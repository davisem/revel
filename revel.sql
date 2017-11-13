CREATE TABLE variants (
	chrom INT(2) NOT NULL,
	hg19_pos INT(15) NOT NULL,
	ref CHAR(5) NOT NULL,
	alt CHAR(5) NOT NULL,
	aaref CHAR(5) NOT NULL,
	aaalt CHAR(5) NOT NULL,
	REVEL FLOAT(4) NOT NULL
);

.mode csv
.import revel_all_chromosomes.csv variants

CREATE INDEX posidx ON variants(chrom, hg19_pos);