{% extends "home/header.html" %}

{% block content %}

    <h2>Send e-mail to vandewynkel@gmail.com</h2>

    <!--<form action="mailto:vandewynkel@gmail.com" method="post" enctype="text/plain">-->
    <form action="https://formspree.io/ryan@vandycraft.com"
      method="POST">
    Name:<br>
    <input type="text" name="name"><br>
    E-mail:<br>
    <input type="text" name="mail"><br>
    Message:<br>

<textarea id="message" type="text" name="message">
</textarea><br><br>

    <input type="submit" value="Send">
    <input type="reset" value="Reset">

    </form>
<?php

echo "test 1 2 3";

?>
{% endblock %}