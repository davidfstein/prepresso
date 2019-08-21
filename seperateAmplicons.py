from Bio import SeqIO
from argparse import ArgumentParser

def parseFastq(file):
    with open(file, 'rU') as fastq:
        return [record for record in SeqIO.parse(fastq, "fastq")]

def seperateBarcodes(records, barcode, id):
    with open(id + ".fastq", 'w') as output:
        for record in records:
            if barcode in record.seq:
                SeqIO.write(record, output, "fastq")

def main():
    userInput = ArgumentParser(description="")
    requiredNamed = userInput.add_argument_group('required arguments')
    requiredNamed.add_argument('-p', '--Path', action='store', required=True,
                                help='Path to fastq.')
    
    args = userInput.parse_args()
    path = args.Path
    records = parseFastq(path)
    seperateBarcodes(records, "GCGATCTA", "Fibin1")
    seperateBarcodes(records, "ATAGAGAG", "Fibin2")
    seperateBarcodes(records, "AGAGGATA", "Fibin3")

if __name__ == '__main__':
    main()