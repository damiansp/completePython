export FLASK_APP=$1

if [ "$2" = "debug" ]; then
    echo Debug mode on
    export FLASK_DEBUG=1
fi
flask run
