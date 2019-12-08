<!--
this was my try to use PHP to insert username and pass data to our database
this is not working as of now
to use use PHP with in Django framework:
1/Install `Django-PHP-Bridge`_:: pip install django-php-bridge
2/copy <form method="post" action="connect.php"> int he login.html
3/copy folowings in the setting.py
    SESSION_ENGINE = 'django_php_bridge.backends.db'
    SESSION_COOKIE_NAME = 'PHPSESSID'
-->


<?php

$username = filter_input(INPUT_POST, 'username');
$password = filter_input(INPUT_POST, 'password');

if (!empty($username)){
if (!empty($password)){

$host="salt.db.elephantsql.com";
$dbusername="ixvgfxto";
$dbpassword="Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0"
$dbname="ixvgfxto";
}
// Create connection
$conn = new postgres ($host, $dbusername, $dbpassword, $dbname);
if (postgres_connect_error()){
  die('Connect Error ('. postgres_connect_errno() .') '
    . postgres_connect_error());
}
else{
  $sql = "INSERT INTO dynamicpystroke_userdatas (username, password)
  values ('$username','$password')";
  if ($conn->query($sql)){
      echo "New record is inserted sucessfully";
  }
  else{
    echo "Error: ". $sql ."<br>". $conn->error;
  }
  $conn->close();
}
}
else{
echo "Password should not be empty";
die();
}
}
else{
echo "Username should not be empty";
die();
}
?>

<!-- //create connection
$conn = new postgres ($host, $dbusername, $dbpassword, $dbname)


DB_NAME = 'ixvgfxto'
DB_USER = 'ixvgfxto'
DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
DB_HOST = 'salt.db.elephantsql.com'
DB_PORT = '5432'
DB_URL = 'postgres://ixvgfxto:Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0@salt.db.elephantsql.com:5432/ixvgfxto'

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)


 ?> -->
