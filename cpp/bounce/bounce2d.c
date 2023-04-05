#include<curses.h>
#include<signal.h>
#include<sys/time.h>
#include "bounce.h"

struct ppball the_ball;

void set_up();
void wrap_up();
int set_ticker(int);
void ball_move(int);
int bounce_or_lose(struct ppball *);

int main()
{
	int c;

	set_up();

	while((c = getchar()) != EOF){
		if( c == 'f') the_ball.x_ttm--;
		else if( c == 's' ) the_ball.x_ttm++;
		else if( c == 'f' ) the_ball.y_ttm--;
		else if( c == 'F' ) the_ball.y_ttm++;
		else if( c == 'Q' ) break;
	}
	wrap_up();
}

void set_up()
{
	void ball_move(int);

	the_ball.y_pos = Y_INIT;
	the_ball.x_pos = X_INIT;
	the_ball.y_ttg = the_ball.y_ttm = Y_TTM;
	the_ball.x_ttg = the_ball.x_ttm = X_TTM;
	the_ball.y_dir = 1;
	the_ball.x_dir = 1;
	the_ball.symbol = DFL_SYMBOL;

	initscr();
	noecho();
	crmode();

	signal(SIGINT, SIG_IGN);
	mvaddch(the_ball.y_pos, the_ball.x_pos,the_ball.symbol);
	refresh();

	signal(SIGALRM, ball_move);
	set_ticker(1000 / TICKS_PER_SEC);
}

void wrap_up()
{
	set_ticker(0);
	endwin();
}

void ball_move(int signum)
{
	int y_cur, x_cur, moved;

	signal(SIGALRM, SIG_IGN);
	y_cur = the_ball.y_pos;
	x_cur = the_ball.x_pos;
	moved = 0;

	if(the_ball.y_ttm > 0 && the_ball.y_ttg-- == 1){
		the_ball.y_pos += the_ball.y_dir;
		the_ball.y_ttg = the_ball.y_ttm;
		moved = 1;
	}
	if(the_ball.x_ttm > 0 && the_ball.x_ttg-- == 1){
		the_ball.x_pos += the_ball.x_dir;
		the_ball.x_ttg = the_ball.x_ttm;
		moved = 1;
	}

	if(moved)
	{
		mvaddch(y_cur, x_cur, BLANK);
		mvaddch(y_cur, x_cur, BLANK);
		mvaddch(the_ball.y_pos, the_ball.x_pos, the_ball.symbol);
		bounce_or_lose(&the_ball);
		move(LINES-1, COLS-1);
		refresh();
	}
	signal(SIGALRM, ball_move);
}

int bounce_or_lose(struct ppball *bp)
{
	int return_val = 0;

	if(bp->y_pos == TOP_ROW){
		bp->y_dir = 1;
		return_val = 1;
	}else if(bp->y_pos == BOT_ROW){
		bp->y_dir = -1;
		return_val = 1;
	}

	if(bp->x_pos == LEFT_EDGE){
		bp->x_dir = 1;
		return_val = 1;
	}else if(bp->x_pos == RIGHT_EDGE){
		bp->x_dir = -1;
		return_val = 1;
	}
	return return_val;
}

int set_ticker(int n_msecs)
{
	struct itimerval new_timeset;
	long n_sec, n_usecs;

	n_sec = n_msecs/1000;	// init part
	n_usecs = (n_msecs % 1000) * 1000L;	// remainder

	new_timeset.it_interval.tv_sec = n_sec;
	new_timeset.it_interval.tv_usec = n_usecs;

	new_timeset.it_value.tv_sec = n_sec;
	new_timeset.it_value.tv_usec = n_usecs;

	return setitimer(ITIMER_REAL, &new_timeset, NULL);
}
