# Comandos de la Práctica 01
## Mirén Jessamyn Hernández Leyva

# Parte I.

**Respuesta 1:**

/bin/bash

**Respuesta 2:**

mkdir data filtered raw_data meta scripts figures archive


**Respuesta 3:**

mv -t data filtered raw_data

**Respuesta 4:**

Como si fuera un convenio no estipulado, la organización de los directorios
se hace de esta manera, para tener una mejor organización en nuestros reposi-
torios, permitiendo que las personas con las que los compartamos o nosotros
mismos en el futuro encontremos de manera más eficiente os datos crudos, datos
procesados, scripts y documentación necesarios para reproducir los análisis
realizados.

Los subdirectorios que usamos son para:

-data: contiene todos los datos especiales.
-filtered: subdivisión de los datos genericos.
-raw_data: subdivisión de los datos genericos.
-meta: guarda todos los metadatos.
-figures: guarda el código que se utilice sólo para hacer las figuras de una
  publicación dada.
-archive: guarda scripts y resultados no necesarios pero que es bueno no borrar
  por completo.


# Parte II.

**Respuesta 1:**

chmod 777 delay.sh

**Respuesta 2:**

ls -l delay.sh

./delay.sh

**Respuesta 3:**

nano delay.sh

echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."
sleep 30s
echo "Ya puedo continuar!"

Ctr+0 Ctr+S

./delay.sh

**Respuesta 4:**

nano delay.sh

echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."
sleep 300s
echo "Ya puedo continuar!"

Ctr+0 Ctr+S

./delay.sh &

killall delay.sh

# Parte III.

**Respuesta 1:**

cd meta
touch SarsCov-2.txt

**Respuesta 2:**

mv sequence.fasta sarscov2_genome.fasta

mv sequence.gff3 sarscov2_genome.gff3

mv sequence.fasta splike_c.faa

mv sequence\ \(1\).fasta splike_b.faa

mv sequence\ \(2\).fasta splike_a.faa

cd meta

touch SarsCov-2_Spike.txt

mv sarscov2_assembly.fasta.gz sarscov2_genome.fasta sarscov2_genome.gff3 splike_a.faa splike_b.faa splike_c.faa 
>SRR10971381_R1.fastq.gz SRR10971381_R2.fastq.gz data/raw_data/

# Parte IV.

**Respuesta 1:**

cd data/filtered/

ln -s /home/hp-spectre/GenomicaComputacional/mhernandez_p01/data/raw_data/splike_a.faa splike_a.faa

ln -s /home/hp-spectre/GenomicaComputacional/mhernandez_p01/data/raw_data/splike_b.faa splike_b.faa

ln -s /home/hp-spectre/GenomicaComputacional/mhernandez_p01/data/raw_data/splike_c.faa splike_c.faa

**Respuesta 2:**

touch glycoproteins.faa

**Respuesta 3:**

head -1 splike_a.faa
>pdb|6VXX|A Chain A, SARS-CoV-2 spike glycoprotein

head -1 splike_b.faa
>pdb|6VXX|B Chain B, SARS-CoV-2 spike glycoprotein

head -1 splike_c.faa
>pdb|6VXX|C Chain C, SARS-CoV-2 spike glycoprotein

**Respuesta 4:**

cat splike_a.faa splike_b.faa splike_c.faa > glycoproteins.faa

**Respuesta 5:**

mv data/raw_data/splike_*.faa archive/

Las ligas simbólicas suaves se rompieron, aun qué el archivo sigue existiendo
las rutas que habíamos determinado ya no, así que en teoría estas ligas están
apuntando a la nada.

zless SRR10971381_R1.fastq.gz

**Respuesta 6:**

less sarscov2_genome.fasta

less sarscov2_assembly.fasta.gz

head -3 sarscov2_genome.fasta
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC

gunzip sarscov2_assembly.fasta.gz

head -3 sarscov2_assembly.fasta
>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG

La diferencia entre el número de lecturas de los archivos .fasta ...

**Respuesta 7:**

grep '>' sarscov2_genome.fasta | wc
>    1      11      97                (Una aparicion)

grep '>' sarscov2_assembly.fasta | wc
>    35      35    1171               (35 apariciones)

**Respuesta 8:**

gunzip SRR10971381_R2.fastq.gz

head -12 SRR10971381_R2.fastq
    >@SRR10971381.512_2
    CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
    +
    /FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
    @SRR10971381.556_2
    TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
    +
    6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
    @SRR10971381.1428_2
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    +
    FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF

Patrón elegido: @SRR10971381

grep '@SRR10971381' SRR10971381_R2.fastq | wc
> 130022  130022 3069925                   (130022 apariciones)

 **Respuesta 9:**

 Los tres formatos almacenan secuencias de datos, pero:
 -.fasta este formato almacena un numero variable de secuencias de nucleotidos
   cada una con su identificador, cada secuencia empieza con el caracter '>'
   seguido del identificador,  las siguientes lineas contienen la secuencia.

 -.faa La NCBI utiliza esta extensión para los aminoácidos FASTA, lo que sig-
   nifica que se trata de un archivo de proteína FASTA.

 -.fastq almacena tanto una secuencia biológica, generalmente de nucleótidos,
   como sus puntuaciones de calidad correspondientes. Utilizan 4 lineas por
   secuencia:
      -La línea 1: comienza con un carácter '@' y va seguida de un identifica-
       dor de secuencia y una descripción opcional.
      -La línea 2 son las letras de la secuencia sin procesar.
      -La línea 3 comienza con un carácter '+' y opcionalmente va seguida de
       nuevo por el mismo identificador de secuencia (y cualquier descripción).
      -La línea 4 codifica los valores de calidad para la secuencia en la lí-
       nea 2 y debe contener el mismo número de símbolos que letras en la se-
       cuencia.


 **Respuesta 10:**

less sarscov2_genome.gff3, desplego el archivo sin organizar, mientras que
less -S sarscov2_genome.gff3 despliega el archivo por línea, haciendo que la
linea se corte al terminar la pantalla, es decir, no la muestra, dándonos así
una mejor visualización para el archivo.

 **Respuesta 11:**

awk '$3 == "gene"' sarscov2_genome.gff3 | less -S
>  NC_045512.2     RefSeq  gene    266     21555   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    21563   25384   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    25393   26220   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    26245   26472   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    26523   27191   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    27202   27387   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    27394   27759   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    27756   27887   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    27894   28259   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    28274   29533   .       +       .       ID=gene-GU280_
  NC_045512.2     RefSeq  gene    29558   29674   .       +       .       ID=gene-GU280_

awk '$3 == "gene"' sarscov2_genome.gff3 | less -S | wc
>  11     100    1822                              (11 genes)

El campo 3 corresponde a ...

La diferencia entre gene y CDS es ...
