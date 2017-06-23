<?php


class Persona2
{
    public $nombre;
    public $edad;
    public $email;

    public function setPersona($nombre, $edad, $email)
    {
        $this->nombre = $nombre;
        $this->edad = $edad;
        $this->email = $email;
    }

    public function mostrarCredencial()
    {
        echo "Tu nombre es: ".$this->nombre;
        echo "Tu edad es: ".$this->edad;
        echo "Tu email es: ".$this->email;
    }
}

$newPersona = new Persona2();
$newPersona->setPersona("Alfredo", 28, "ejemplo@mail.com");
$newPersona->mostrarCredencial();
