<?php
$chars = "abcdefghijkmpqrstuvwxyzABCDEFGHJKLMPQRSTUVWXYZ23456789";
for ($seed = 0; $seed <= 1577098880; $seed += 1)         
{
        srand($seed);
        $pw = "";
        for($i=0; $i<12; ++$i)
        {
                $key = rand(0, 53);
                $pw = $pw . $chars[$key];
        }
        print $pw . "\n";
}
?>
