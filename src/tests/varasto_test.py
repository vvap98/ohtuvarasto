import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    def test_konstruktori_virheellinen_tilavuus(self):
        varasto = Varasto(0)
        self.assertAlmostEqual(varasto.tilavuus, 0)

        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_virheellinen_alkusaldo(self):
        varasto = Varasto(10, -2)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_alkusaldo_tasmalleen_tilavuus(self):
        varasto = Varasto(10, 10)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_konstruktori_alkusaldo_yli_tilavuuden(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_tasmalleen_vapaaseen_tilaan(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_negatiivinen_maara(self):
        tulos = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(tulos, 0)

    def test_ottaminen_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        tulos = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(tulos, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str(self):
        self.assertEqual(
            str(self.varasto),
            "saldo = 0, vielä tilaa 10"
        )
##turha kommentti