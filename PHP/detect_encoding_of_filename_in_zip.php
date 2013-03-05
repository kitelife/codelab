<?php
//
// 检测zip压缩包中文件的文件名的编码，貌似不一定准确
//
function detect_encoding($zipfile_name){
    $zip = new ZipArchive;
    $res = $zip->open($zipfile_name);
    if(true !== $res)
        throw new Exception('Can Not Open Zip File '.$res);

    $encoding = "UTF-8";
    $controller = array("ASCII","UTF-8", "GB2312", "GBK", "BIG5");

    for($i = 0; $i < $zip->numFiles; ++ $i){
        // $entry是文件名字符串
        $entry = $zip->getNameIndex($i);
        // 函数mb_detect_encoding依次尝试$controller中给定的编码，若找到，
        // 则余下的编码类型不再尝试
        // 若Windows下的简体中文，则$encoding等于EUC_CN
        $encoding = mb_detect_encoding($entry, $controller);
        if( "UTF-8" !== $encoding)
            $entry = iconv($encoding, "UTF-8", $entry);
        echo $entry." ---> ".$encoding.chr(10);
    }
    $zip->close();
}
detect_encoding($argv[1]);
?>
