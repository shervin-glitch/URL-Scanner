version = '1.1.2'

import os
import sys
import time
import datetime
import requests
from colorama.ansi import Fore
from colorama.initialise import init
from cfonts.cli import (main, render , say)

init()

os.system("clear")

dateNow = datetime.datetime.now().strftime("%d/%b/%y")

timeNow = datetime.datetime.now().strftime("%H:%M:%S")

header = render("Validator" , font = "3d" , colors = ["magenta" , "cyan"] , align = "center")
time.sleep(1.5)
print(header)
time.sleep(1)
UserInput = input(f"{Fore.GREEN}[+] {Fore.WHITE}Enter The full URL Here => {Fore.CYAN}")

counter = 0

try:

    while True:
        counter += 1
        break

    try:
        req = requests.get(f"{str(UserInput)}")

# Status Code 100
        if req.status_code == 100:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}100"
                  f"\nThis interim response indicates"
                  f"\nthat everything so far is OK and that "
                  f"\nthe client should continue the request,"
                  f"\nor ignore the response if the request is already finished.")
        elif req.status_code == 101:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}101"
                  f"\nThis code is sent in response to an Upgrade request header from "
                  f"\nthe client, and indicates "
                  f"\nthe protocol the server is switching to.")
        elif req.status_code == 102:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}102"
                  f"\nThis code indicates that the server has received"
                  f"\nand is processing the request,"
                  f"\nbut no response is available yet.")
        elif req.status_code == 103:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}103"
                  f"\nThis status code is primarily intended to be used with the Link header,"
                  f"\nletting the user agent start"
                  f"\npreloading resources while the server prepares a response.")
#{Fore.WHITE} Status Code 200
        elif req.status_code == 200:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}200"
                  f"\nThe request has succeeded."
                  f"\nThe meaning of the success depends on the HTTP method:"
                  f"\nGET , HEAD , PUT , POST , TRACE")
        elif req.status_code == 201:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}201"
                  f"\nThe request has succeeded and a new resource has been created as a result."
                  f"\nThis is typically the response sent after POST requests,"
                  f"\nor some PUT requests.")
        elif req.status_code == 202:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}202"
                  f"\nThe request has been received but not yet acted upon. It is noncommittal, "
                  f"\nsince there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. "
                  f"\nIt is intended for cases where another process or server handles the request, or for batch processing.")
        elif req.status_code == 203:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}203"
                  f"\nThis response code means the returned meta-information is not exactly the same as is available from the origin server,"
                  f"\nbut is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource."
                  f"\nExcept for that specific case, the 200 OK response is preferred to this status.")
        elif req.status_code == 204:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}204"
                  f"\nThere is no content to send for this request, but the headers may be useful."
                  f"\nThe user-agent may update its cached headers for "
                  f"\nthis resource with the new ones.")
        elif req.status_code == 205:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}205"
                  f"\nTells the user-agent to "
                  f"\nreset the document which "
                  f"\nsent this request.")
        elif req.status_code == 206:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}206"
                  f"\nThis response code is used when the Range header is"
                  f"\nsent from the client to "
                  f"\nrequest only part of a resource.")
        elif req.status_code == 207:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}207"
                  f"\nConveys information about multiple resources,"
                  f"\nfor situations where multiple status codes"
                  f"\nmight be appropriate.")
        elif req.status_code == 208:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}208"
                  f"\nUsed inside a <dav:propstat> response element to "
                  f"\navoid repeatedly enumerating the internal members of "
                  f"\nmultiple bindings to the same collection.")
        elif req.status_code == 226:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}226"
                  f"\nThe server has fulfilled a GET request for the resource,"
                  f"\nand the response is a representation of the result of "
                  f"\none or more instance-manipulations applied to the current instance.")
#{Fore.WHITE} Status Code 300
        elif req.status_code == 300:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}300"
                  f"\nThe request has more than one possible response."
                  f"\nThe user-agent or user should choose one of them. (There is no standardized way of choosing one of the responses,"
                  f"\nbut HTML links to the possibilities are recommended so the user can pick.)")
        elif req.status_code == 301:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}301"
                  f"\nThe URL of the requested resource has"
                  f"\nbeen changed permanently. "
                  f"\nThe new URL is given in the response.")
        elif req.status_code == 302:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}302"
                  f"\nThis response code means that the URI of requested resource has been changed temporarily."
                  f"\nFurther changes in the URI might be made in the future. "
                  f"\nTherefore, this same URI should be used by the client in future requests.")
        elif req.status_code == 303:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}303"
                  f"\nThe server sent this response to direct the "
                  f"\nclient to get the requested resource at another "
                  f"\nURI with a GET request.")
        elif req.status_code == 304:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}304"
                  f"\nThis is used for caching purposes."
                  f"\nIt tells the client that the response has not been modified,"
                  f"\nso the client can continue to use the same cached version of the response.")
        elif req.status_code == 305:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}305"
                  f"\nDefined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy."
                  f"\nIt has been deprecated due to security concerns "
                  f"\nregarding in-band configuration of a proxy.")
        elif req.status_code == 306:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}306"
                  f"\nThis response code is no longer used;"
                  f"\nit is just reserved."
                  f"\nIt was used in a previous version of the HTTP/1.1 specification.")
        elif req.status_code == 307:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}307"
                  f"\nThe server sends this response to direct the client to get the requested resource at another URI "
                  f"\nwith same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the "
                  f"\nexception that the user agent must not change the HTTP method used: "
                  f"\nIf a POST was used in the first request, a POST must be used in the second request.")
        elif req.status_code == 308:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}308"
                  f"\nThis means that the resource is now permanently located at another URI,"
                  f"\nspecified by the Location: HTTP Response header. "
                  f"\nThis has the same semantics as the 301 Moved Permanently HTTP response code, "
                  f"\nwith the exception that the user agent must not change the HTTP method used: "
                  f"\nIf a POST was used in the first request, a POST must be used in the second request.")
#{Fore.WHITE} Status Code 400
        elif req.status_code == 400:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}400"
                  f"\nThe server could not understand"
                  f"\nthe request due to"
                  f"\ninvalid syntax.")
        elif req.status_code == 401:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}401"
                  f"\nAlthough the HTTP standard specifies ""unauthorized"","
                  "\nsemantically this response means ""unauthenticated"". "
                  "\nThat is, the client must authenticate itself to get the requested response.")
        elif req.status_code == 402:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.MAGENTA}402"
                  f"\nThis response code is reserved for future use. "
                  f"\nThe initial aim for creating this code was using it for digital payment systems, "
                  f"\nhowever this status code is used very rarely and no standard convention exists.")
        elif req.status_code == 403:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}403"
                  f"\nThe client does not have access rights to the content;"
                  f"\nthat is, it is unauthorized, so the server is refusing to give the requested resource."
                  f"\nUnlike 401, the client's identity is known to the server.")
        elif req.status_code == 404:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}404"
                  f"\nThe server can not find the requested resource. In the browser, this means the URL is not recognized. "
                  f"\nIn an API, this can also mean that the endpoint is valid but the resource itself does not exist. "
                  f"\nServers may also send this response instead of 403 to hide the existence of a resource from an unauthorized client. "
                  f"\nThis response code is probably the most famous one due to its frequent occurrence on the web.")
        elif req.status_code == 405:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}405"
                  f"\nThe request method is known by the server but has been disabled and cannot be used."
                  f"\nFor example, an API may forbid DELETE-ing a resource. "
                  f"\nThe two mandatory methods, GET and HEAD, must never be disabled and should not return this error code.")
        elif req.status_code == 406:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}406"
                  f"\nThis response is sent when the web server, "
                  f"\nafter performing server-driven content negotiation, "
                  f"\ndoesn't find any content that conforms to the criteria given by the user agent.")
        elif req.status_code == 407:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}407"
                  f"\nThis is similar to 401"
                  f"\nbut authentication is needed to be "
                  f"\ndone by a proxy.")
        elif req.status_code == 408:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}408"
                  f"\nThis response is sent on an idle connection by some servers, "
                  f"\neven without any previous request by the client. It means that the server would like to shut down this unused connection. "
                  f"\nThis response is used much more since some browsers, like Chrome,"
                  f"\nFirefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. "
                  f"\nAlso note that some servers merely shut down the connection without sending this message.")
        elif req.status_code == 409:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.GREEN}409"
                  f"\nThis response is sent when "
                  f"\na request conflicts with the current "
                  f"\nstate of the server.")
        elif req.status_code == 410:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}410"
                  f"\nThis response is sent when the requested content has been permanently deleted from server,"
                  f"\nwith no forwarding address. Clients are expected to remove their caches and links to the resource."
                  f"\nThe HTTP specification intends this status code to be used for ""limited-time, promotional services""."
                  "\nAPIs should not feel compelled to indicate resources that have been deleted with this status code.")
        elif req.status_code == 411:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}411"
                  f"\nServer rejected the request because the "
                  f"\nContent-Length header field is not defined and "
                  f"\nthe server requires it.")
        elif req.status_code == 412:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}412"
                  f"\nThe client has indicated preconditions"
                  f"\nin its headers which the server "
                  f"\ndoes not meet.")
        elif req.status_code == 413:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}413"
                  f"\nRequest entity is larger than limits defined by server;"
                  f"\nthe server might close the connection or return an "
                  f"\nRetry-After header field.")
        elif req.status_code == 414:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}414"
                  f"\nThe URI requested by the client is"
                  f"\nlonger than the server is "
                  f"\nwilling to interpret.")
        elif req.status_code == 415:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}415"
                  f"\nThe media format of the requested data is not "
                  f"\nsupported by the server,"
                  f"\nso the server is rejecting the request.")
        elif req.status_code == 416:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}416"
                  f"\nThe range specified by the Range header field in the request can't be fulfilled;"
                  f"\nit's possible that the range is "
                  f"\noutside the size of the target URI's data.")
        elif req.status_code == 417:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}417"
                  f"\nThis response code means the expectation "
                  f"\nindicated by the Expect request header "
                  f"\nfield can't be met by the server.")
        elif req.status_code == 418:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}418"
                  f"\nThe server refuses "
                  f"\nthe attempt to brew "
                  f"\ncoffee with a teapot.")
        elif req.status_code == 421:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}421"
                  f"\nThe request was directed at a server that is not able to produce a response. "
                  f"\nThis can be sent by a server that is not configured to produce responses for the combination of "
                  f"\nscheme and authority that are included in the request URI.")
        elif req.status_code == 422:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}422"
                  f"\nThe request was well-formed "
                  f"\nbut was unable to be followed due to "
                  f"\nsemantic errors.")
        elif req.status_code == 423:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}423"
                  f"\nThe resource that "
                  f"\nis being accessed is "
                  f"\nlocked.")
        elif req.status_code == 424:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}424"
                  f"\nThe request failed "
                  f"\ndue to failure of "
                  f"\na previous request.")
        elif req.status_code == 425:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}425"
                  f"\nIndicates that the server is unwilling to "
                  f"\nrisk processing a request that might "
                  f"\nbe replayed.")
        elif req.status_code == 426:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}426"
                  f"\nThe server refuses to perform the request using the current protocol but might be willing to "
                  f"\ndo so after the client upgrades to a different protocol. "
                  f"\nThe server sends an Upgrade header in a 426 response to indicate the required protocol(s).")
        elif req.status_code == 428:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}428"
                  f"\nThe origin server requires the request to be conditional. "
                  f"\nThis response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, "
                  f"\nmodifies it, and PUTs it back to the server, when meanwhile a third party has modified the state on the server, "
                  f"\nleading to a conflict.")
        elif req.status_code == 429:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}429"
                  f"\nThe user has sent too many requests "
                  f"\nin a given amount of time "
                  f"\n(""rate limiting"").")
        elif req.status_code == 431:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}431"
                  f"\nThe server is unwilling to process the request because its header fields are too large. "
                  f"\nThe request may be resubmitted after reducing the size of the request header fields.")
        elif req.status_code == 451:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.MAGENTA}451"
                  f"\nThe user-agent requested a resource that cannot legally be provided,"
                  f"\nsuch as a web page censored by a government.")
        elif req.status_code == 500:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}500"
                  f"\nThe server has endateNowed[{timeNow}] a situation it doesn't know how to handle.")
        elif req.status_code == 501:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}501"
                  f"\nThe request method is not supported by the server and cannot be handled. "
                  f"\nThe only methods that servers are required to support "
                  f"\n(and therefore that must not return this code) are GET and HEAD.")
        elif req.status_code == 502:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}502"
                  f"\nThis error response means that the server, "
                  f"\nwhile working as a gateway to get a response needed to handle the request, "
                  f"\ngot an invalid response.")
        elif req.status_code == 503:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}503"
                  f"\nThe server is not ready to handle the request. "
                  f"\nCommon causes are a server that is down for maintenance or that is overloaded. "
                  f"\nNote that together with this response, "
                  f"\na user-friendly page explaining the problem should be sent. "
                  f"\nThis responses should be used for temporary conditions and the Retry-After: "
                  f"\nHTTP header should, if possible, contain the estimated time before the recovery of the service. "
                  f"\nThe webmaster must also take care about the caching-related headers that are sent along with this response, "
                  f"\nas these temporary condition responses should usually not be cached.")
        elif req.status_code == 504:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}504"
                  f"\nThis error response is given when the server is acting as a "
                  f"\ngateway and cannot get a response in time.")
        elif req.status_code == 505:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}505"
                  f"\nThe HTTP version used in the request is not supported by the server.")
        elif req.status_code == 506:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}506"
                  f"\nThe server has an internal configuration error: "
                  f"\nthe chosen variant resource is configured to engage in transparent content negotiation itself, "
                  f"\nand is therefore not a proper end point in the negotiation process.")
        elif req.status_code == 507:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}507"
                  f"\nThe method could not be performed on the resource because the server is "
                  f"\nunable to store the representation needed to successfully complete the request.")
        elif req.status_code == 508:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.RED}508"
                  f"\nThe server detected an infinite loop while processing the request.")
        elif req.status_code == 510:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}510"
                  f"\nFurther extensions to the request are required for the server to fulfill it.")
        elif req.status_code == 511:
            time.sleep(1)
            print(f"{Fore.CYAN}[{dateNow}][{timeNow}]{Fore.WHITE} Status Code : {Fore.YELLOW}511"
                  f"\nThe 511 status code indicates that the client needs to authenticate to gain network access.")

        else:
            print(str(ZeroDivisionError))

    except ConnectionError as CE:
        print(str(CE))

    finally:
        with open("log.txt", "r") as LOG:
            LOG.close()


except PendingDeprecationWarning as PDW:
    print(str(PDW))
    sys.exit()

finally:
    if __name__ == "__main__":
        pass