<?php
namespace App\Controller;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;


class HomeController extends AbstractController
{
    #[Route('/', name: 'home')] 
    public function renderHomePage(): Response
    {
        return $this->render('home_page.html.twig', [
            'imageEndpoint' => $this->generateUrl('retrieve_plot'), 
        ]);
    }
}


