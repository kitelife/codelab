<?php
// 中文翻译地址： http://wulijun.github.com/php-the-right-way/
// 1.
// 内置Web服务器
// php -S localhost::8001
//
// 2.
// 日期和时间
$raw = '22. 11. 1968';
$start = \DateTime::createFromFormat('d. m. Y', $raw);
echo "Start date: " . $start->format('m/d/Y') . "\n";

$today = new \DateTime();
echo "Today: " . $today->format('Y-m-d') . "\n";

// DateTime计算时间时通常需要DateInterval类，如add()和sub方法，都是将DateInterval作为参数。尽量避免直接用时间戳表示时间，夏令时和时区会让时间戳产生歧义，使用间隔日期更为妥当。计算两个日期的差值使用diff()方法，返回DateInterval对象，输出显示也很方便。

// create a copy of $start and add one month and 6 days
$end = clone $start;
$end->add(new \DateInterval('P1M6D'));

$diff = $end->diff($start);
echo "Difference: " . $diff->format('%m month, %d days (total: %a days)') . "\n";

// DateTime对象之间可以直接比较
if($start < $end) {
    echo "Start is before end!\n";
}

// DatePeriod类的用法：用于循环事项(recurring events)的迭代。构造函数的参数为：start和end，均为DateTime对象，以及返回事项的间隔周期。
//
//根据first thursday如何创建一个时间间隔？
$periodInterval = \DateInterval::createFromDateString('first thursday');
$periodIterator = new \DatePeriod($start, $periodInterval, $end, \DatePeriod::EXCLUDE_START_DATE);
foreach($periodIterator as $date)
{
    // output each date in the period
    echo $date->format('m/d/Y') . " ";
}
echo "\n";

// 3.
// 数据库操作PDO
// PDO是数据库连接抽象库，从PHP 5.1.0开始提供，提供多种数据库的统一的操作接口。PDO不会转化你的SQL查询或者模拟缺失特性；它只是提供统一的API去连接不同的数据库而已。
// 更重要的是，PDO允许你绑定SQL查询语句中的变量，而无需担心SQL注入问题，这主要通过PDO statements和变量绑定来实现。
// 假设PHP脚本接收一个数字ID作为查询参数，从数据库取回一条记录。下面是一种错误的做法：
// $pdo = new PDO('sqlite::users.db');
// $pdo->query("SELECT name FROM users WHERE id = " . $_GET['id']);
// 这是非常糟糕的代码，直接在SQL中插入一个原始输入变量，导致潜在的SQL注入风险。假如黑客构造URL：http://domain.com/?id=1%3BDELETE+FROM+users来传入恶意参数id，则$_GET['id']的变量值为1;DELETE FROM users，这将删除数据表中的所有用户！因此，应该使用PDO的绑定参数功能来处理ID输入参数。
// $pdo = new PDO('sqlite:users.db');
// $stmt = $pdo->prepare('SELECT name FROM users WHERE id = :id');
// $stmt->bindParam(':id', filter_input(INPUT_GET, 'id', FILTER_SANITIZE_NUMBER_INT), PDO::PARAM_INT);
// $stmt->execute();

// 4.
// 数据过滤
// 永远不要在PHP代码中信任外部输入，在使用之前一定要先过滤和验证，filter_var和filter_input函数可以帮助过滤文本和验证文本格式（如邮箱地址）。
// 外部输入可以是：$_GET和$_POST表单输入数据、$_SERVER超级变量中的某些值和通过fopen('php://input', 'r')获取的HTTP请求体。要记住外部输入不仅仅是用户提交的表单数据，还包括上传和下载的文件、session变量、cookie数据和第三方Web服务提供的数据等。

// 5.
// 缓存
// 5.1
// 字节码缓存
// 在一个PHP文件被执行时，它先被编译为字节码（也称为opcode），然后这些字节码被执行。如果文件没有修改，那么字节码也会保持不变，这意味着编译这一步白白浪费了CPU资源。
// 通过把字节码保存在内存中来消除冗余的编译，重用它们完成后续的调用。配置字节码缓存非常简单，而且可以极大地提高应用的执行效率，没有理由不使用字节码缓存。
// 5.2
// 对象缓存
// 使用最多的内存对象缓存系统是APC和memcached，APC是很好的一个对象缓存方案，它提供了简单的API来让你把对象存储在内存中，而且配置和使用都非常容易，它的一个缺点是只能在本机使用。Memcached则是另外一种方式，它是一个单独的服务，可以通过网络访问，这意味着可以在一个地方写入数据，然后在不同的系统中访问这份数据。
// 在单机性能上，APC通常比Memcached更高，如果你不需要多台服务器或者其他Memcached的高级功能，APC可能是你的最佳选择。
//
?>
