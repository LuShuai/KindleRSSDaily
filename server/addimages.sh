#!/bin/bash

addimg(){
    htmlfile=$1
    img=$2

    #load counter
    c=$(cat c.tmp)
    c=$(($c + 1))

    #construct unique file name
    localname=${htmlfile%.*}-$c-$(echo $img | sed 's/^\(.*\)\&.*$/\1/g' | sed 's/^\(.*\)?.*$/\1/g'| xargs basename)

    #download the image file
    echo "downloading $localname from $img"
    wget $img -O $localname

    #compress the images
    convert $localname -resize "400x400>" -colorspace Gray temp.img
    mv temp.img $localname

    # replace url of images
    #echo "sed 's|$img|$localname|g' < $htmlfile > tmp.html"
    sed "s|$img|$localname|g" < $htmlfile > tmp.html
    mv tmp.html $htmlfile

    echo $c > c.tmp
}

f=$1
if grep -q  "<img\([^>]\)\+>" $f; then
    echo 0 > c.tmp;
    export -f addimg;
    grep -o  "<img\([^>]\)\+>" $f | sed 's/.*src="\([^"]*\)".*/\1/g' | sort -u | xargs -L1 -I % bash -c "addimg '$f' '%'";
    rm c.tmp;
fi
