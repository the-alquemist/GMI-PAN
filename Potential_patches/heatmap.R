# Open as PDF #
pdf("HMP_test.pdf")
# Load matrix into a variable #
table <- read.table("table", header = T)
# Patricio's housekeeping commands #
suppressPackageStartupMessages(library(circlize))
suppressPackageStartupMessages(library(ComplexHeatmap))
# Load libraries #
library("ComplexHeatmap")
library(circlize)
# Rebuild matrix to ignore vertical and horizontal header #
row_n <- nrow(table)
column_n <- ncol(table)
df <- table[1:row_n,2:column_n]
# Save df as a matrix in mat #
mat <- as.matrix(df)
# Create string vector for column names #
vector1 <- table$Contig
# Color setting (White/Green) / Source: RColorBrewer #
col_fun = colorRamp2(c(0,0.49,0.51,1), c("#ffffff","#ffffff","#31a354","#31a354"))
# Header(column annotation) is already saved, row annotation is not specified #
ha = rowAnnotation(
	foo = anno_text(
	vector1,
	rot=0,
	gp=gpar(fontsize=8)
	)
)
# Build the heatmap argument #
at=c(0.25,0.75)
ht = Heatmap(
	mat,  
	column_title="ISP Plasmids", 
	column_title_gp =gpar(fontsize = 20, fontface = "bold"),
	col=col_fun, 
	cluster_rows=TRUE, 
	cluster_columns=TRUE, 
	border=TRUE,
        show_row_names=FALSE,
	show_column_names=FALSE,
	show_row_dend=TRUE,
	show_column_dend=FALSE, 
	row_dend_side="left",
	row_dend_width = unit(3.5, "cm"),
	right_annotation=ha,
	heatmap_legend_param=list(
        	at=at,
        	legend_gp=gpar(fill=col_fun(at)),
		title="Accesory Genes",
		title_gp=gpar(fontsize = 12,fontface="bold"),
		title_position = "leftcenter-rot",
        	labels=c("Absence","Presence"),
		labels_gp=gpar(fontsize=9.5),
		border="black"
	)
)
# Force drawing of the heatmap #
draw(ht)
# Close and save PDF #
dev.off()
