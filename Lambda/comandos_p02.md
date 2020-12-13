# Comandos de la Práctica 03
## Lambda
### Integrante 1: Hernández Leyva Mirén Jessamyn
### Integrante 2: Muñoz Barón Luis Miguel
### Integrante 3: Acosta García Daniel Enrique

# Parte I.

cd GenomicaComputacional/

mkdir Lambda

git add *

git commit -m "Agregando comandos_p2.md y la tabla de comparativa"

git push origin master


### Tabla:

|             Plataforma/compañía            | Longitud de reads (pb) | # reads x run |  Tiempo  | Costo x 10^6 bases | Error (%) |         Química        |
|:------------------------------------------:|:----------------------:|:-------------:|:--------:|:------------------:|:---------:|:----------------------:|
|             Primera generación             |                        |               |          |                    |           |                        |
|          Sanger/Life Technologies          |           800          |       1       |   2 hrs  |        2400        |    0.3    |   Dideoxy terminator   |
|             Segunda generación             |                        |               |          |                    |           |                        |
|          454 GS FLX+/Roche/0.7 Gb          |           700          |     1×106     |  24/48 h |         10         |     1     |     Pyrosequencing     |
|            GS Junior/Roche/70 Mb           |           500          |     1×105     |   18 h   |          9         |           |     Pyrosequencing     |
|           HiSeq/Illumina/1500 Gb           |          2x150         |     5×109     | 27/240 h |         0.1        |    0.8    | Reversible terminators |
|            MiSeq/Illumina/15 Gb            |          2x300         |     3×108     |   27 h   |        0.13        |    0.8    | Reversible terminators |
|       SOLiD/Life Technologies/120 Gb       |           50           |     1×109     |  14 days |        0.13        |    0.01   |        Ligation        |
|          Retrovolocity/BGI/3000 Gb         |           50           |     1×109     |  14 days |        0.01        |    0.01   |    Nanoball/ligation   |
|     Ion Proton/Life Technologies/100 Gb    |           200          |     6×107     |   2–5 h  |          1         |    1.7    |    Proton detection    |
|       Ion PGM/Life Technologies/2 Gb       |           200          |     5×106     |   2–5 h  |          1         |    1.7    |    Proton detection    |
|             Tercera generación             |                        |               |          |                    |           |                        |
|              SMRT/Pac Bio/1 Gb             |         >10,000        |     1×106     |   1–2 h  |          2         |    12.9   |      Real-time SMS     |
|           Heliscope/Helicos/25 Gb          |           35           |     7×109     |  8 days  |        0.01        |    0.2    |      Real-time SMS     |
| Nanopore/Oxford Nanopore Technologies/1 Gb |          >5000         |     6×104     |  48/72 h |         <1         |     34    |      Real-time SMS     |
|           Electron microscopy/ZS           |          7200          |               |   14 h   |        <0.01       |           |      Real-time SMS     |					1

Deschamps, S., Llaca, V.,& May, G.. (2012). Genotyping-by-Sequencing in Plants. Biology. 1. 460-83. 10.3390/biology1030460.

FH Munster University of Applied Sciences. (s.f.). Analysis of next-generation sequencing data. 8/12/2020, de FH Munster Sitio web: https://www.fh-muenster.de/eti/downloads/labore/db/bioinf/BFG_Chapter09_NGS_v04.pdf

Parte 2

# Parte II.

### Respuesta 1.

Las secuencias crudas del genoma se encuentran en la sección Associated Data, 
Data Availability Statement, en el link:  http://www.ebi.ac.uk/ena/data/view/PRJEB5172

Descomprimimos usando: 

gunzip ERR486827_1.fastq.gz

gunzip ERR486828_1.fastq.gz


Conviertimos de fastq a fasta usando:

sed -n '1~4s/^@/>/p;2~4p' ERR486827_1.fastq > ERR486827_1.fasta

sed -n '1~4s/^@/>/p;2~4p' ERR486828_1.fastq > ERR486828_1.fasta


### Respuesta 2.

ERR486827_1.fasta tiene 398824 secuencias 

tail ERR486827_1.fasta

>ERR486827.398820 MS7_12182:1:2114:15553:28079#29/1
GATGCATTGTATTGCTTCACCTTGTTGGGTTGGTAGAGTTGGAAGGAGGCTAACCACATTTCTCGCCATTTCCCCTTCATCAAACAAGATACCGATGCTTTCTAACGCTTGCTTGGTGTTGAGGTATTTATTAAATGATCCAGAAGAAGC
>ERR486827.398821 MS7_12182:1:2114:21096:28084#29/1
GGTGGGGTTGAAAGAGGAAGAAGATTCCACTTCCATAACTATTCAACGGCGTAGCGTTAATCAAGGAATTGATCGCTACTGATGATTTTTCTGTGTTTTTCACCGGATAAGCAGTTTTAATGATGGTTCCTGATGAAATTTGATTACTAT
>ERR486827.398822 MS7_12182:1:2114:13866:28362#29/1
CCCGTTTTACTATCTAAGCTAGTTGTTGTTGATCAAGCAAGTGCTTGGTTTTGAGTAGAAGAAGAAGAAGAAGAAGAAGAAGAAGAAGAAGAAGCATCATACCCCACACTCCCCGCTTTAAAGCCACTGAAGATCAACTGATCATTGACA
>ERR486827.398823 MS7_12182:1:2114:15461:28589#29/1
AATCCTGATTCTTGGTTATAGGTAACTTCTTTGAAGGTAGTGAGATCCACTGCACTCTCAGCAGTAGTGAACGGAGTAAATGAGAAGGAGATAGGTGCTACATCATTATCAGTTGTTGAAAGTAATGAATCATCACCAGGGTTAAAGTTT
>ERR486827.398824 MS7_12182:1:2114:16165:28804#29/1
CTTGGATTGAAAAACTCCCATTGATTGGACCATTTAATCCCGTGTCGTTGGTCACCAAATCCTTATACCCCGTTTTACTATCTAAGCTAGTTGTTGTTGATCAAGCAAGTGCTTGGTCTTTGGTACTACTACTATCATACCCCACACTCC

Mientras que ERR486827_2.fasta tiene 410959 secuencias 

tail ERR486828_1.fasta
>ERR486828.410955 MS7_12182:1:2114:11919:28316#30/1
GGAGGGGGAACATCAGATCAAAGTAATAAATTCACCAAGTACCTCAACACCAAGCAAGCATTGGAGCGTATCGGCATCTTGTTTGATGGAACAATGGCGAGAAATGTTGTTAGCCCCCTCCTTCCAGCTCTACCAACCCAACAAGGTGAA
>ERR486828.410956 MS7_12182:1:2114:16106:28386#30/1
CTTCCCCAACTTTGCTTTGATGTTTTTAGTTGTTAGGAGTTTTAACAAGTTGGTCATATTGTTCAAATCACTTGCTTGGTTTCACTGCTCCGGCTCAATTAACTTGTTGTAGGTGCCGCTGCTTTGGTAAGCATTTGTTTTCACCTTGTT
>ERR486828.410957 MS7_12182:1:2114:16942:28412#30/1
GGATTATTCTTATTGGTGAAGGTTAATGCGTTGATCCAGTCACTGGTGGGACTGATGGAATTGGGTAAAAAGGAATAGGTAGTTGTTTTTTTGGCGGAGCTACCTGATGGTGTGACTTGATTTTCAGCAGAGGAGGGATTAAACGAAGGA
>ERR486828.410958 MS7_12182:1:2114:16312:29017#30/1
CATAAATCCAATAACTAGCAAAATTAAAAGAAAAATTATGATAAGTTGTCTACCTTTTACTAAAACAATTTTGTTGATCTCTTTATCAACTCCAAATCATAAATTAACAATTCGTTTTTTAAAAGGTAGCTTGGGTTTCTTTTCCTTTGC
>ERR486828.410959 MS7_12182:1:2114:13937:29193#30/1
ATTCCCTTCGACCAGGTGAAACCTAGTAGTCCTTCGTTTAATCCCTCCTCTGCTGAAAATCAAGTCACACCATCAGGTAGCTCCGCCAAAAAAACAACTACCTATTCCTTTTTACCCAATTCCATCAGTCCCACCAGTGACTGGATCAAC

Por lo tanto podemos concluir que no, no tienen la misma cantidad de secuencias.

### Respuesta 3.
Se utiliza un script de python promedio.py para este ejercicio.

python3 promedio.py ERR486827_1.fasta
Promedio de la longitud de las secuencias: 151.0

python3 promedio.py ERR486828_1.fasta
Promedio de la longitud de las secuencias: 151.0

https://github.com/mjhl1999/GenomicaComputacional.git


# Parte III.
### Respuesta 3. 
Abrir el archivo .html en cualquier buscador. Realicen una breve descripción de la calidad de ambas lecturas. Describan si las lecturas ¿Son buenas o malas? ¿Por qué? ¿Cómo es el comportamiento de las calidades?

Las lecturas son casi perfectas dado que al ver el boxplot de los phretscores para ambos archivos fastq podemos notar que la puntuación obtenida ronda 32 - 39 para ambos archivos
por lo que no es necesario llevar a cabo una fase de limpiado a los datos.
Cabe destacar que la puntuación se eleva conforme mas lecturas fueron hechas durante la secuenciación.

### Respuesta 4.
Calculen y reporten la cobertura del genoma tomando en cuenta que:
covertura = (cantidad de lecturas*longitud de lecturas) / total del tamaño del genoma (bp)

(398824 + 410959) * 151 / 580,070 pb  = 210.7973744548

Obtenido de https://www.sciencemag.org/site/feature/data/genomes/270-5235-397.pdf

# Parte IV

### Respuesta 1
Descarguen las secuencias crudas de algún organismo modelo de su preferencia que tenga un genoma pequeño. No suban los datos a GitHub, únicamente hagan una breve descripción de las características del organismo que eligieron.

E. Coli
Por lo general, las bacterias Escherichia coli (E. coli) viven en los intestinos de las personas y de los animales sanos. La mayoría de las variedades de Escherichia coli son inofensivas o causan diarrea breve en términos relativos. Sin embargo, algunas cepas particularmente peligrosas, como la Escherichia coli O157:H7, pueden causar cólicos abdominales intensos, diarrea con sangre y vómitos.

### Respuesta 2
Describan qué tecnología de secuenciación fue utilizada y de ser posible la referencia del artículo donde lo reportan.

generated using the Sanger dideoxy sequencing method (Reference sequence accession: NC_000913). 

fuente: https://www.biostars.org/p/160377/

### Respuesta 3
Calculen la cobertura de su genoma y el desglose que utilizaron para obtenerla.


Se tomo el archivo ERR022075_1.fastq de https://www.ebi.ac.uk/ena/browser/view/ERX008638

Lo convertimos a fasta con:

sed -n '1~4s/^@/>/p;2~4p' data/ERR022075_1.fastq > data/ERR022075_1.fasta

y al analizar el promedio de la longitud de sus secuencias obtuvimos:    

python3 promedio.py ERR022075_1.fasta
Promedio de la longitud de las secuencias: 101.0


