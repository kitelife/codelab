#!/usr/bin/php

<?php

require_once("jpgraph/jpgraph.php");
require_once("jpgraph/jpgraph_pie.php");
require_once("jpgraph/jpgraph_line.php");

$type_dict = Array();
//$time_list = Array();

$month_dict = Array();

function traverse_dir_recursively($dir_name)
{
    global $type_dict;
    //global $time_list;
    global $month_dict;

    if ($file_handler = opendir($dir_name)) {
        while (false !== ($file = readdir($file_handler))) {
            if ($file !== '.' && $file !== '..' && $file[0] !== '.') {
                $file_path = $dir_name . '/' . $file;
                if (is_dir($file_path)) {
                    //echo $file_path . "\n";
                    traverse_dir_recursively($file_path);
                }
                else {
                    //echo $file_path . "\n";
                    //array_push($time_list, filemtime($file_path));
                    $mdate = date("Y-m", filemtime($file_path));
                    if (array_key_exists($mdate, $month_dict)) {
                        $month_dict[$mdate] += 1;
                    }
                    else {
                        $month_dict[$mdate] = 1;
                    }

                    $type = mb_strrchr($file, ".");
                    if ($type) {
                        if (array_key_exists($type, $type_dict)) {
                            $type_dict[$type] += 1;
                        }
                        else {
                            $type_dict[$type] = 1;
                        }
                    }
                }
            }
        }
    }
}

function plot_pie($data, $legend_data) {
    // Create the Pie Graph. 
    $graph = new PieGraph(700, 500);

    //$theme_class="PastelTheme";
    //$graph->SetTheme(new $theme_class());

    // Set A title for the plot
    $graph->title->Set("Visual files by file-type");
    $graph->SetBox(true);

    // Create
    $p = new PiePlot($data);
    $graph->Add($p);

    $p->ShowBorder();
    $p->SetColor('black');
    $p->setLegends($legend_data);
    //$p1->SetSliceColors(array('#1E90FF','#2E8B57','#ADFF2F','#DC143C','#BA55D3'));
    $graph->Stroke(_IMG_HANDLER);
    $graph->img->Stream("visual_file.png");
}

function plot_line($dates, $counts)
{
    $date_num = count($dates);
    $init_x = 600;
    $init_y = 500;
    $scale = ceil( $date_num / 8);

    $graph = new Graph($init_x*$scale, $init_y*$scale);
    $graph->SetScale("textlin");

    $theme_class = new UniversalTheme;

    $graph->SetTheme($theme_class);
    $graph->img->SetAntiAliasing(false);
    $graph->title->Set("frequency of modifing files");
    $graph->SetBox(false);

    $graph->img->SetAntiAliasing();

    $graph->yaxis->HideZeroLabel();
    //$graph->yaxis->HideLine(false);
    //$graph->yaxis->HideTicks(false, false);

    $graph->xgrid->Show();
    $graph->xgrid->SetLineStyle("solid");
    $graph->xaxis->SetTickLabels($dates);
    $graph->xgrid->SetColor("#E3E3E3");

    $p = new LinePlot($counts);
    $graph->Add($p);
    $p->SetColor("#6495ED");

    $graph->Stroke(_IMG_HANDLER);
    $graph->img->Stream("visual_frequency.png");
}

function main($argc, $argv)
{
    global $type_dict;
    //global $time_list;
    global $month_dict;

    if ($argc == 2 && is_dir($dir_name = $argv[1])) {
        traverse_dir_recursively($dir_name) . "\n";
    }

    arsort($type_dict);
    /*
    $a_count = 0;
    foreach($type_dict as $key => $value) {
        $a_count += $value;
        //echo $key . " ---> " . $value . "\n";
    }
    echo $a_count . "\n";
     */
    $filetype_to_show = array_slice($type_dict, 0, 10);
    plot_pie(array_values($filetype_to_show), array_keys($filetype_to_show));
    
    ksort($month_dict);
    /*
    foreach ($month_dict as $key => $value) {
        echo $key . " ===> " . $value . "\n";
    }
     */
    plot_line(array_keys($month_dict), array_values($month_dict));
    /*
    foreach ($time_list as $key => $value) {
        echo $value . " ===> ". date("Y-m-d", $value) . " ===> " . date("Y-m-d H:i:s", $value) . "\n";
    }
     */
}

main($argc, $argv);

/*
$fh = fopen("results.txt", 'w');
fwrite($fh, json_encode($type_dict));
fclose($fh);
 */
