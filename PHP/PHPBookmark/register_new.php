<?php
// include function files for this application
require_once('bookmark_fns.php');

// create short variable names
$email = $_POST['email'];
$username = $_POST['username'];
$passwd = $_POST['passwd'];
$passwd2 = $_POST['passwd2'];
// start session which may be needed later
// start it now because it must go before headers
session_start();
try{
    // check forms filled in
    if(!filled_out($_POST))
    {
        throw new Exception('You have not filled the form out correctly '
                            .'- please go back and try again.');
    }
    // email address not valid
    if(!valid_email($email))
    {
        throw new Exception('That is not a valid email address. Please go back '
                            .' and try again.');
    }
    // passwords not the same
    if($passwd != $passwd2)
    {
        throw new Exception('The passwords you entered do not match '
                            .'- Please go back and try again.');
    }
    
    // check password length is Ok
    if(strlen($passwd)<6)
    {
        throw new Exception('Your password must be at least 6 characters long.'
                            .'Please go back and try again.');
    }
    
    // check username length is ok
    if(strlen($username)>16)
    {
        throw new Exception('Your username must be less than 17 characters long.'
                            .'Please go back and try again.');
    }
    
    // attempt to register
    // this function can also throw an exception
    register($username, $email, $passwd);
    // register session variable
    $_SESSION['valid_user'] = $username;
    
    //provide link to members page
    do_html_header('Registration successful');
    echo 'Your registration was successful. Go to the members page '
            .'to start setting up your bookmarks!';
    do_html_URL('member.php', 'Go to members page');
    
    // end page
    do_html_footer();
}
catch(Exception $e){
    do_html_header('Problem:');
    echo $e->getMessage();
    do_html_footer();
    exit;
}
?>