src=$2
dest=$2.enc
if [ ${#src} -gt 0 -a $1 -a  $1 = "e" ]; then
    openssl enc -aes-128-ecb -in $src -out $dest
elif [ ${#src} -gt 0 -a $1 -a $1 = "d" ]; then
    dest=${src%.enc}
    openssl enc -aes-128-ecb -d -in $2 -out $dest
else
    echo "examples:"
    echo "enc.sh e file"
    echo "enc.sh d file.enc"
    echo "usages:"
    echo "e : encrypt file to file.enc";
    echo "d : deencrypt file.enc to file";
fi



