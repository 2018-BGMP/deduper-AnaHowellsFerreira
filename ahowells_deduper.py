# TODO:
# work on samtools calling with subprocess
# work on functions to handle positive and negative strands
# go over SAM documentation and CIGAR tutorials


######################
#  import libraries  #
######################

# sort file with SAMtools on the command line from Python script
import subprocess as sp

# For regular expressions.
import re

# use call() from SAMtools to sort files based on chromosome.
# test_file = Dataset1_test.sam
#sp.call("samtools sort -l 0  for uncompressed output file
# -m maxMem
# -o sorted.sam , shell=True)

#samtools sort [-l level] [-m maxMem] [-o out.bam] [-O format] [-n] [-t tag] [-T tmpprefix] [-@ threads] [in.sam|in.bam|in.cram]


############
# functions #
############


def paired_end_check function(FLAG)
	if FLAG = ((flag & 1?) == 1?)
	print "paired end found. Exiting!"
	break


def UMI_check function(QNAME)
    UMI = re.search(".*:([A,C,G,T]{8})\t")
return str


def chrom_number(QNAME)
  if QNAME (already in my_set()
  reset my_set()
  write int to my_set()
  return integer


def strand_check function
    if FLAG = ((flag & 16) != 16): #strand is reverse!!!
        strand = "-"
    else:
        strand = "+"

def adj_strand-_pos()
  read cigar string values from - orientation only
  define adj.position (-) = POS + M + S (after) + I + D + N -1  #integers
  return integer of adjusted rightmost POS value


def adj_strand+_pos()
	read cigar string values from + orientation only
    define adj.position (+) = POS - S - 1 (before)
	return integer of adjusted leftmost POS value





####################
#      SCRIPT     #
####################

# initialize empty set to keep track of UMI, chromosome, position, strandedness
my_set = set ()

# open sorted file, ouput file and file containing indexes
with open("sorted.sam") as in_fh, \
    open("dedup_output.sam",'w') as out_fh, \
    open("STL96.txt", "r") as indexes:

    unknown_UMI = 0
    PCR_dup = 0
    total_reads = 0


	for line in in_fh:
		if line.startswith("@"), write to out_fh
		else:
			line = line.strip('\n').split("\t")
        # define parameters to be evaluated by functions
				QNAME = line[0]     # UMI information
				FLAG = int(line[1]) # strandedness information
				POS = int(line[3])  # position at which sequence was read
				CIGAR = line[4]     # information to consider when adjusting POS

        # double check for paired-end data
        if paired_end_check == TRUE
            break
        else
            continue

        # check for correct/expected UMI in QNAME
        if UMI_check == TRUE:
            my_set.add(UMI)
        else
            unknown_UMI += 1
            read.nextline ### how to call this??
            continue

         # reset my set if reading a different chromossome
         if chrom_number in my_set
            my_set.clear()
        else
            continue

        # check for strand orientation and adjust position if necessary
        if strand_check = "+"   # this is the forward strand
            #do these set of operations to evaluate if there was
            #softclipping and if this a real duplicate
            adj_strand+_pos()
         else
            continue

         if strand_check = "-"  # this is the reverse strand
            #do these OTHER set of operations to evaluate if there was
            #softclipping and if this a real duplicate
            adj_strand-_pos()


         total_reads += 1


print("Total PCR duplicates:" PCR_dup, "\t" "Total reads:", total_reads, "\t", "Unknown UMIs found:", unknown_UMI)
