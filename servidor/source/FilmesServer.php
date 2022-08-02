<?php

namespace Filme;

use Exception;
use SplObjectStorage;
use Ratchet\ConnectionInterface;
use Ratchet\MessageComponentInterface;

final class FilmesServer implements MessageComponentInterface
{
    private $clientes;

    public function __construct()
    {
        $this->clientes = new SplObjectStorage();
    }

    public function onOpen(ConnectionInterface $conn): void
    {
        $this->clientes->attach($conn);
    }

    public function onMessage(ConnectionInterface $from, $msg): void
    {
        foreach ($this->clientes as $cliente) {
            $cliente->send($msg);
        }
    }

    public function onClose(ConnectionInterface $conn): void
    {
        $this->clientes->detach($conn);
    }

    public function onError(ConnectionInterface $conn, Exception $exception): void
    {
        $conn->close();
    }
}
?>