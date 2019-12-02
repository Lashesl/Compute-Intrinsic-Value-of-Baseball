 library(viridis)
 path = "/Users/apple/Desktop/uci class/199"
 setwd=(path)
 mysurface = read.table(file='richardheat.txt', header = FALSE, sep = "")
 
 mysurface = as.matrix(mysurface)
 
 source("sample-heatmap.R")

#Set the Color limits
zmax = 0.038 #maximum value
zmin = -0.03 #minimum value
levelwidth = 0.0001 # minimum changes between values
levels = (zmax-zmin)/levelwidth

#setup the text size for axis tick labels
textSize = 3.0

png(filename = "Heatmap_test_Xueying Liu.png",width = 1700, height = 1200)

par(mar=c(16.4,24,4.8,24))#change the distance between the border and graph.(bottom,left,top,right)

x=seq(from=-1.5, to=1.5,length=31)
y=seq(from=1.0,to=4.0,length=31)

filled.contourR(x,  #how to choose the range of x,y
                y,
                z=mysurface,
                xlim = range(x, finite = TRUE), 
                ylim = range(y, finite = TRUE),
                zlim=c(zmin,zmax),
                nlevels = levels,
                axes= TRUE,
                color.palette = viridis,
                asp =1,
                key.title = title(main = ""),
                
                plot.axes = {axis(side = 1, at = seq(-1.5, 1.5, by = 0.5), cex.axis=textSize, padj = 0.7, tck = -0.015, lwd = 3)
                  axis(side=2, at=seq(1.0, 4.0, by = 0.5),cex.axis=textSize, tck = -0.015, lwd = 3)
                },
                key.axes = axis(4, c(-0.029, -0.022, -0.016, -0.009, -0.002, 0.004, 0.011, 0.018, 0.025, 0.031, 0.038) ,cex.axis=textSize, tck = -0.2, lwd = 3)  ,
                
                cex.lab=textSize,
                
                xaxs = "itestsss", #the type of scale mark
                
                 plot.title= {
                 windowsFonts(times=windowsFont("Times New Roman"))
                   title(xlab=italic('l')~"    (feet)",cex.lab=textSize, line=11.5, family="times")
                   mtext(expression(italic('x')~"         "), side = 1, cex=textSize, line=11.5, family="times")
               title(ylab=italic('l')~"    (feet)",cex.lab=textSize, line=9, family="times")
                   mtext(expression(italic('z')~"         "), side = 2, cex=textSize, line=9, las = 0, family="times")
                 }
              )


dev.off() #end of plot
