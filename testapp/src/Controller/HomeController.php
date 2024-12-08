<?php
// src/Controller/LuckyController.php
namespace App\Controller;
use Symfony\Component\Routing\Attribute\Route;

use Symfony\Component\HttpFoundation\Response;

class HomeController
{
    #[Route('/', name:'home')]
    public function number(): Response
    {
        $number = 60;

        return new Response(
            '<html><body>Lucky number: '.$number.'</body></html>'
        );
    }
}



