<?php
namespace App\Controller;

use App\Service\PythonApiClient;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Psr\Log\LoggerInterface;
use Symfony\Component\HttpFoundation\Request;


class ImageController extends AbstractController
{
    #[Route('/retrieve_plot', name: 'retrieve_plot')]
    public function displayPlot(PythonApiClient $pythonApiClient, LoggerInterface $logger, Request $request): Response
    {
        try {
            $logger->info("sending post request to api");

            $endpoint = $request->query->get("endpoint", "/plot");
            $function = $request->query->get('function', 'x'); 
            $title = $request->query->get('title', 'Default Title');
            $payload = [
                'function' => $function,
                'title' => $title,
            ];

            $imageData = $pythonApiClient->post($endpoint, $payload);

            return new Response(
                $imageData,
                Response::HTTP_OK,
                ['Content-Type' => 'image/png']  
            );
        } catch (\Exception $e) {
            $logger->error("Error: " . $e->getMessage());
            $logger->info("couldnt send the request to the api");
            return new Response('Error: ' . $e->getMessage(), Response::HTTP_INTERNAL_SERVER_ERROR);
        }
    }
}
