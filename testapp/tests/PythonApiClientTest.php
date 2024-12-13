<?php

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use Symfony\Contracts\HttpClient\HttpClientInterface;
use Symfony\Contracts\HttpClient\ResponseInterface;
use App\Service\PythonApiClient;

class PythonApiClientTest extends Testcase
{
    public function testPost () : void
    {
        $mockHttpClient = $this->createMock(HttpClientInterface::class);

        $mockResponse = $this->createMock(ResponseInterface::class);

        $mockResponse
        ->method('toArray')
        ->willReturn([
            'plot'=> base64_encode('mock string')
        ]);

        $mockResponse
        ->method('getStatusCode')
        ->willReturn(200);


        $mockHttpClient
        ->method('request')
        ->with('POST', "http://localhost:5000/mock_endpoint", [
            'json' => ['function' => 'x^2',
                        "title"  => "mocktitle" ],
        ])
        ->willReturn($mockResponse);

        
        $apiClient = new PythonApiClient($mockHttpClient);
        $result = $apiClient->post("/mock_endpoint",  ['function' => 'x^2',  "title"  => "mocktitle" ]);
        
        $this->assertEquals( 'mock string', $result);

    }




}


