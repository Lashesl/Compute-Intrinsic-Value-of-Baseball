 library(viridis)
 path = "C:/Users/xueyinl8/Desktop"
 setwd=(path)
 mysurface = read.table(file='Xueying56x76.txt', header = FALSE, sep = "")
 
 mysurface = as.matrix(mysurface)
 mysurface = apply(mysurface, 1, rev)
 
source("filled.contourR.R")

#Set the Color limits
zmax = 1.0 #maximum value
zmin = 0.0 #minimum value
levelwidth = 0.0001 # minimum changes between values
levels = (zmax-zmin)/levelwidth

#setup the text size for axis tick labels
textSize = 3.0

#windows()

png(filename = "RainbowHeatmap_Xueying Liu.png",width = 1700, height = 1200)

par(mar=c(22.5,16,12,52))#change the distance between the border and graph.(bottom,left,top,right)

x=seq(from=-45, to=45,length=76)# the length of x equal to the number of row
y=seq(from=-10,to=45,length=56)

filled.contourR(x,  #how to choose the range of x,y
                y,
                z=mysurface,
                xlim = range(x, finite = TRUE), 
                ylim = range(y, finite = TRUE),
                zlim=c(zmin,zmax),
                nlevels = levels,
                axes= TRUE,
                color=colorRampPalette(c("darkblue", "darkblue","blue", "dodgerblue2", 
                			  "lightskyblue", "lightskyblue", "cyan3", "green4", 
                			  "greenyellow", "greenyellow", "yellow", "gold", 
                			  "orange", "red", "darkred")),
              #  color.palette = viridis,
                asp =1,
                key.title = title(main = ""),
                
                plot.axes = {axis(side = 1, at = seq(-45, 45, by = 15), cex.axis=textSize, padj = 0.7, tck = -0.015, lwd = 3)
                  axis(side=2, at=seq(-10, 45, by = 10),cex.axis=textSize, tck = -0.015, lwd = 3)
                },
                key.axes = axis(4, c(0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0) ,cex.axis=textSize, tck = -0.2, lwd = 3)  ,
                
                cex.lab=textSize,
                
                xaxs = "itestsss", #the type of scale mark
                
                 plot.title= {
                         #windowsFonts(times=windowsFont("Times New Roman"))
            #       title(xlab=italic('l')~"    (feet)",cex.lab=textSize, line=8.0, family="times")
                    title(xlab="horizontal angle",cex.lab=textSize, line=8.0, family="times")
            #       mtext(expression(italic('x')~"         "), side = 1, cex=textSize, line=8, family="times")
               title(ylab="vertical angle",cex.lab=textSize, line=8, family="times")
             #      mtext(expression(italic('z')~"         "), side = 2, cex=textSize, line=8, las = 0, family="times")
                 }
              )


dev.off() #end of plot
