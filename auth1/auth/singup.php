<?php
include "../connect.php";

$username = fliterRequset("username");
$email = fliterRequset("email");
$password =fliterRequset("password");
$phone =fliterRequset("phone");
$user =fliterRequset("user") ;
$stmt = $con->prepare("INSERT INTO 
`user`( `name`, `email`, `password`, `phone`,`typeofuser`) 
VALUES ($username,$email,$password,$phone,$user)");
$stmt->execute();

$count =$stmt->rowCount();

if ($count > 0) {
 
    echo json_encode(array("status"=>"success"));
}
else{
    echo json_encode(array("status"=>"fail"));
}
 

 