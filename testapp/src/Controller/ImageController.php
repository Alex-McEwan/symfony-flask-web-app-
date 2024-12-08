<?php
namespace App\Controller;

use App\Service\PythonApiClient;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Psr\Log\LoggerInterface;

class ImageController extends AbstractController
{
    #[Route('/displayplot', name: 'display_plot')]
    public function displayPlot(PythonApiClient $pythonApiClient, LoggerInterface $logger): Response
    {
        try {
            $logger->info("Starting to get the image from the API...");

            $endpoint = '/plot';
            $payload = ['function' => 'x', "title" => "title"]; 

            $logger->debug("Sending request to Python API with endpoint: $endpoint and payload: " . json_encode($payload));

            $imageData = $pythonApiClient->post($endpoint, $payload);

            $logger->info("Image successfully decoded. Binary data length: " . strlen($imageData));

            return new Response(
                $imageData,
                Response::HTTP_OK,
                ['Content-Type' => 'image/png']  
            );
        } catch (\Exception $e) {
            $logger->error("Error occurred: " . $e->getMessage());

            return new Response('Error: ' . $e->getMessage(), Response::HTTP_INTERNAL_SERVER_ERROR);
        }
    }
}