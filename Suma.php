<?php
class Suma
{
    public $numero1, $numero2;

    public function sumar($numero1, $numero2)
    {
        return $numero1 + $numero2;
    }
}


$operacion = new Suma();
print $operacion->sumar(1,2);

