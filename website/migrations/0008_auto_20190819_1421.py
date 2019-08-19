# Generated by Django 2.2.4 on 2019-08-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20190818_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='pais_de_origem',
            field=models.CharField(choices=[('AFE', 'Afeganistão'), ('ADS', 'África do Sul'), ('ALB', 'Albânia'), ('ALE', 'Alemanha'), ('AND', 'Andorra'), ('ANGO', 'Angola'), ('ANG', 'Anguilla'), ('AH', 'Antilhas Holandesas'), ('ANT', 'Antárctida'), ('AB', 'Antígua e Barbuda'), ('ARG', 'Argentina'), ('ARGE', 'Argélia'), ('ARM', 'Armênia'), ('ARU', 'Aruba'), ('AS', 'Arábia Saudita'), ('AUS', 'Austrália'), ('AUST', 'Áustria'), ('AZE', 'Azerbaijão'), ('BAH', 'Bahamas'), ('BAHR', 'Bahrein'), ('BANG', 'Bangladesh'), ('BARB', 'Barbados'), ('BEL', 'Belize'), ('BEN', 'Benim'), ('BER', 'Bermudas'), ('BIE', 'Bielorrússia'), ('BOL', 'Bolívia'), ('BOT', 'Botswana'), ('BRU', 'Brunei'), ('BUL', 'Bulgária'), ('BURK', 'Burkina Faso'), ('BURU', 'Burundi'), ('BUT', 'Butão'), ('BEL', 'Bélgica'), ('BOSH', 'Bósnia e Herzegovina'), ('CB', 'Cabo Verde'), ('CAMA', 'Camarões'), ('CAMB', 'Camboja'), ('CAN', 'Canadá'), ('CAT', 'Catar'), ('CAZ', 'Cazaquistão'), ('CHA', 'Chade'), ('CHIL', 'Chile'), ('CHIN', 'China'), ('CHI', 'Chipre'), ('COL', 'Colômbia'), ('COM', 'Comores'), ('CDN', 'Coreia do Norte'), ('CDS', 'Coreia do Sul'), ('CDM', 'Costa do Marfim'), ('CR', 'Costa Rica'), ('CRO', 'Croácia'), ('CBA', 'Cuba'), ('DIN', 'Dinamarca'), ('DJI', 'Djibouti'), ('DOM', 'Dominica'), ('EGI', 'Egito'), ('ES', 'El Salvador'), ('EMA', 'Emirados Árabes Unidos'), ('EQU', 'Equador'), ('ERI', 'Eritreia'), ('ESC', 'Escócia'), ('ESL', 'Eslováquia'), ('ESLOVE', 'Eslovênia'), ('ESP', 'Espanha'), ('EFM', 'Estados Federados da Micronésia'), ('EUA', 'Estados Unidos'), ('EST', 'Estônia'), ('ETI', 'Etiópia'), ('FIJ', 'Fiji'), ('FIL', 'Filipinas'), ('FIN', 'Finlândia'), ('FRA', 'França'), ('GAB', 'Gabão'), ('GA', 'Gana'), ('GE', 'Geórgia'), ('GIB', 'Gibraltar'), ('GRA', 'Granada'), ('GRO', 'Gronelândia'), ('GRE', 'Grécia'), ('GUAD', 'Guadalupe'), ('GUAM', 'Guam'), ('GUAT', 'Guatemala'), ('GUE', 'Guernesei'), ('GUI', 'Guiana'), ('GUIF', 'Guiana Francesa'), ('GUE', 'Guiné'), ('GUEEQ', 'Guiné Equatorial'), ('GUIB', 'Guiné-Bissau'), ('GAM', 'Gâmbia'), ('HAI', 'Haiti'), ('HON', 'Honduras'), ('HK', 'Hong Kong'), ('HUN', 'Hungria'), ('IB', 'Ilha Bouvet'), ('IM', 'Ilha de Man'), ('IN', 'Ilha do Natal'), ('IHIM', 'Ilha Heard e Ilhas McDonald'), ('INOR', 'Ilha Norfolk'), ('ICAY', 'Ilhas Cayman'), ('ICO', 'Ilhas Cocos(Keeling)'), ('ICOOK', 'Ilhas Cook'), ('IFE', 'Ilhas Feroé'), ('IGSSS', 'Ilhas Geórgia do Sul e Sandwich do Sul'), ('IMA', 'Ilhas Malvinas'), ('IMAR', 'Ilhas Marshall'), ('IMDEU', 'Ilhas Menores Distantes dos Estados Unidos'), ('IS', 'Ilhas Salomão'), ('IVA', 'Ilhas Virgens Americanas'), ('IVB', 'Ilhas Virgens Britânicas'), ('IAL', 'Ilhas Åland'), ('INDO', 'Indonésia'), ('ING', 'Inglaterra'), ('INDI', 'Índia'), ('IRAQ', 'Iraque'), ('IRN', 'Irlanda do Norte'), ('IRL', 'Irlanda'), ('IRA', 'Irã'), ('ISL', 'Islândia'), ('ISR', 'Israel'), ('ITA', 'Itália'), ('IEM', 'Iêmen'), ('JAM', 'Jamaica'), ('JAP', 'Japão'), ('JER', 'Jersey'), ('JOR', 'Jordânia'), ('KIR', 'Kiribati'), ('KUW', 'Kuwait'), ('LAO', 'Laos'), ('LES', 'Lesoto'), ('LET', 'Letônia'), ('LIB', 'Libéria'), ('LIE', 'Liechtenstein'), ('LIT', 'Lituânia'), ('LUX', 'Luxemburgo'), ('LIBA', 'Líbano'), ('LIBI', 'Líbia'), ('MAC', 'Macau'), ('MAC', 'Macedônia'), ('MAD', 'Madagáscar'), ('MALA', 'Malawi'), ('MALD', 'Maldivas'), ('MALI', 'Mali'), ('MALTA', 'Malta'), ('MALAS', 'Malásia'), ('MARIS', 'Marianas Setentrionais'), ('MARR', 'Marrocos'), ('MART', 'Martinica'), ('MAUR', 'Mauritânia'), ('MAURI', 'Maurícia'), ('MAYO', 'Mayotte'), ('MOL', 'Moldávia'), ('MON', 'Mongólia'), ('MONT', 'Montenegro'), ('MONTS', 'Montserrat'), ('MOÇ', 'Moçambique'), ('MYA', 'Myanmar'), ('MEX', 'México'), ('MON', 'Mônaco'), ('NAM', 'Namíbia'), ('NAU', 'Nauru'), ('NEP', 'Nepal'), ('NIC', 'Nicarágua'), ('NIG', 'Nigéria'), ('NIU', 'Niue'), ('NOR', 'Noruega'), ('NC', 'Nova Caledônia'), ('NZ', 'Nova Zelândia'), ('NIG', 'Níger'), ('OMA', 'Omã'), ('PAL', 'Palau'), ('PALE', 'Palestina'), ('PAN', 'Panamá'), ('PNG', 'Papua-Nova Guiné'), ('PAQ', 'Paquistão'), ('PAR', 'Paraguai'), ('PDG', 'País de Gales'), ('PB', 'Países Baixos'), ('PE', 'Peru'), ('PIT', 'Pitcairn'), ('PF', 'Polinésia Francesa'), ('POL', 'Polônia'), ('PR', 'Porto Rico'), ('POR', 'Portugal'), ('QUI', 'Quirguistão'), ('QUE', 'Quênia'), ('RU', 'Reino Unido'), ('RCA', 'República Centro-Africana'), ('RC', 'República Checa'), ('RDC', 'República Democrática do Congo'), ('RCO', 'República do Congo'), ('RD', 'República Dominicana'), ('REU', 'Reunião'), ('ROM', 'Romênia'), ('RUA', 'Ruanda'), ('RUS', 'Rússia'), ('SAA', 'Saara Ocidental'), ('SM', 'Saint Martin'), ('SB', 'Saint-Barthélemy'), ('SPM', 'Saint-Pierre e Miquelon'), ('SAM', 'Samoa Americana'), ('SA', 'Samoa'), ('SHATC', 'Santa Helena, Ascensão e Tristão da Cunha'), ('SL', 'Santa Lúcia'), ('SEN', 'Senegal'), ('SLE', 'Serra Leoa'), ('SEY', 'Seychelles'), ('SIN', 'Singapura'), ('SOM', 'Somália'), ('SRI', 'Sri Lanka'), ('SUAZ', 'Suazilândia'), ('SUD', 'Sudão'), ('SUR', 'Suriname'), ('SUE', 'Suécia'), ('SUI', 'Suíça'), ('SVA', 'Svalbard e Jan Mayen'), ('SCN', 'São Cristóvão e Nevis'), ('SM', 'São Marino'), ('STP', 'São Tomé e Príncipe'), ('SVG', 'São Vicente e Granadinas'), ('SERV', 'Sérvia'), ('SIR', 'Síria'), ('TAD', 'Tadjiquistão'), ('TAI', 'Tailândia'), ('TAIW', 'Taiwan'), ('TAN', 'Tanzânia'), ('TAAF', 'Terras Austrais e Antárticas Francesas'), ('TBOI', 'Território Britânico do Oceano Índico'), ('TL', 'Timor-Leste'), ('TOG', 'Togo'), ('TON', 'Tonga'), ('TOQ', 'Toquelau'), ('TRI', 'Trinidad e Tobago'), ('TUN', 'Tunísia'), ('TUR', 'Turcas e Caicos'), ('TURQ', 'Turquemenistão'), ('TURQUI', 'Turquia'), ('TUV', 'Tuvalu'), ('UCR', 'Ucrânia'), ('UGA', 'Uganda'), ('URU', 'Uruguai'), ('UZB', 'Uzbequistão'), ('VAN', 'Vanuatu'), ('VAT', 'Vaticano'), ('VEN', 'Venezuela'), ('VIET', 'Vietname'), ('WAF', 'Wallis e Futuna'), ('ZIM', 'Zimbabwe'), ('ZAM', 'Zâmbia')], max_length=255, null=True, verbose_name='País de Origem'),
        ),
    ]
