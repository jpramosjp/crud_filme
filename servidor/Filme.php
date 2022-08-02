<?php

require './vendor/autoload.php';

use Filme\FilmesServer;

$app = new Ratchet\App('localhost', 9990);
$app->route('/filme', new FilmesServer, ['*']);
$app->run();
?>
