<?php 
function fliterRequset($requestrname){

    return json_encode(strip_tags($_POST[$requestrname]));



} 