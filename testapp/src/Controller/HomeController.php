<?php
namespace App\Controller;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;



class HomeController extends AbstractController
{
    #[Route('/', name: 'home', methods: ['GET', 'POST'])] 
    public function renderHomePage(Request $request): Response
    {

        $imageEndpoint = $this->generateUrl('retrieve_plot');
        if ($request->isMethod('POST')) {
            $function = $request->request->get('function', 'x'); 
            $title = $request->request->get('title', 'title'); 

            $imageEndpoint = $this->generateUrl('retrieve_plot', [
                'function' => $function,
                'title' => $title,
            ]);
        }
        return $this->render('home_page.html.twig', [
            'imageEndpoint' => $imageEndpoint, 
        ]);
    }
}


