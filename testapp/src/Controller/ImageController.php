<?php

namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;


class ImageController
{



    #[Route('/displayplot')]
    public function fetchImage(): Response
    {
        // Temporary test response
        return new Response('<html><body>Test: Controller is available</body></html>');
    }
}
