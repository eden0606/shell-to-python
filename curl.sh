#!/bin/bash

final=$(curl --silent --show-error -u $user:$password -i -H 'set custom header here' -X GET -k "http://eden0606.github.io" | grep "name" | awk -F ":" {'print $2'} | awk -F\" {'print $2'}) 
 
#silent -> Don't show progress meter or error messages. Makes curl mute. It will still output the data you ask for, potentially even to the terminal/stdout unless you redirect it.
# --show-error -> When used with -s, it makes curl show error message if it fails.
# -u -> user:password **must be this format**
#-i ->  Include the HTTP-header in the output. The HTTP-header includes things like server-name, date of the document, HTTP-version and more.
#-H -> Extra header to use when getting a web page.
#-X -> Specifies a custom request method to use when communicating with the HTTP server. The specified request will be used instead of the method otherwise used (which defaults to GET). 
echo "timed out"
#-k -> This option explicitly allows curl to perform "insecure" SSL connections and transfers. All SSL connections are attempted to be made secure by using the CA certificate bundle installed by default.
#grep -> looks for the specified string of characters in a file
#-F ":" -> awk default separator is white space, -F allows you to change what separates outputs, so in this case : is put between the outputs
#{'print $2'} -> prints second field
#-F \" -> puts \ between fields, i think it's kind of like -F "\" maybe syntatically different/error but still works?
