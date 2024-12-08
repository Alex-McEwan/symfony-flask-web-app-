<?php



namespace App\Contract;

interface PythonApiClientInterface
{
    public function post(string $endpoint, array $payload): string;
}
