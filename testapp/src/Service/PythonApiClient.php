<?php

namespace App\Service;

use Symfony\Contracts\HttpClient\HttpClientInterface;

class PythonApiClient
{
    private HttpClientInterface $httpClient;
    private string $pythonAPIstring = "http://localhost:5000";

    public function __construct(HttpClientInterface $httpClient)
    {
        $this->httpClient = $httpClient;
    }
    public function post(string $endpoint, array $payload): string
    {
        $url = $this->pythonAPIstring . $endpoint;

        $response = $this->httpClient->request(
            'POST',
            $url,
            [
                'json' => $payload,
            ]
        );

        if ($response->getStatusCode() !== 200) {
            throw new \Exception('Error communicating with Python API: ' . $response->getStatusCode());
        }

        
        $responseArray = $response->toArray();
        $imageBase64 = $responseArray['plot'];
        $imageData = base64_decode($imageBase64);
        return $imageData;

    }
}



