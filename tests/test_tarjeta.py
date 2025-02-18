import unittest
from src import TarjetaDeCredito

class TestInteresTarjeta(unittest.TestCase):
    def test_caso_normal(self):
        tarjeta = TarjetaDeCredito(cupo_disponible=1_000_000, tasa_interes=3.1)
        total_intereses = tarjeta.calcular_total_intereses(monto=200000, cuotas=36)
        self.assertAlmostEqual(total_intereses, 134726.53, delta=0.1)

    def test_tasa_cero(self):
        tarjeta = TarjetaDeCredito(cupo_disponible=1_000_000, tasa_interes=0)
        total_intereses = tarjeta.calcular_total_intereses(monto=480000, cuotas=48)
        self.assertEqual(total_interes, 0)

    def test_tasa_usura(self):
        tarjeta = TarjetaDeCredito(cupo_disponible=1_000_000, tasa_interes=12.5)
        with self.assertRaises(ValueError) as context:
            tarjeta.calcular_total_intereses(monto=50000, cuotas=60)
        self.assertTrue("tasa de usura" in str(context.exception))

    def test_monto_invalido(self):
        tarjeta = TarjetaDeCredito(cupo_disponible=1_000_000, tasa_interes=2.4)
        with self.assertRaises(ValueError) as context:
            tarjeta.calcular_total_intereses(monto=0, cuotas=60)
        self.assertTrue("superior a cero" in str(context.exception))

    def test_cuotas_negativas(self):
        tarjeta = TarjetaDeCredito(cupo_disponible=1_000_000, tasa_interes=1)
        with self.assertRaises(ValueError) as context:
            tarjeta.calcular_total_intereses(monto=50000, cuotas=-10)
        self.assertTrue("mayor a cero" in str(context.exception))

if __name__ == '__main__':
    unittest.main()

"""
Métodos de prueba:

test_caso_normal: Verifica el cálculo con valores regulares usando assertAlmostEqual para manejar decimales.

test_tasa_cero: Valida que no se generen intereses con tasa 0%.

test_tasa_usura: Comprueba que se lance error con tasas altas.

test_monto_invalido: Verifica validación de monto positivo.

test_cuotas_negativas: Valida el rechazo de cuotas negativas.

Herramientas clave:

assertAlmostEqual: Compara números flotantes con tolerancia (delta=0.1).

assertRaises: Verifica que se lancen excepciones específicas.

Mensajes de error: Se comprueba que el error contenga texto clave.

Lógica esperada en la clase:

Conversión de tasa porcentual a decimal (3.1% → 0.031).

Fórmula de cuota mensual:

python
Copy
cuota = (monto * i) / (1 - (1 + i)**-cuotas)
Cálculo de intereses totales: (cuota * cuotas) - monto

Validaciones previas al cálculo (tasas, montos y cuotas).
"""