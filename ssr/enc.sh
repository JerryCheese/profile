if [ $1 -a $1 = "enc" ]; then
    openssl enc -aes-128-ecb -in ssr.json -out ssr.json.enc
elif [ $1 -a $1 = "denc" ]; then
    openssl enc -aes-128-ecb -d -in ssr.json.enc -out ssr.json
else
    echo "usages:"
    echo "enc  - encrypt ssr.json to ssr.json.enc";
    echo "denc - deencrypt ssr.json.enc to ssr.json";
fi



