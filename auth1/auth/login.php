<?php
include "../connect.php";


$email = fliterRequset("email");
$password =fliterRequset("password");


$stmt = $con->prepare("SELECT * FROM user WHERE `email`= $email AND `password` =$password;"); //'password' هنا وضعنا السنغل كوتيشن لان الباس وورد كلمة محجوزة 
$stmt->execute();

$data=$stmt->fetch(PDO::FETCH_ASSOC);
$count =$stmt->rowCount();

if ($count > 0) {
 
    echo json_encode(array("status"=>"success","data"=>$data));
}
else{
    echo json_encode(array("status"=>"fail"));
}
 

 