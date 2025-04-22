#   Date: Mon-8-July-2024


#   Briefing
This is a small practice work to see how to use email verification links.


#   Elabs

##  Things Learnt
    1.  Block names in Jinja should not have hyphens; they must be like Python identifiers insteas...
    so use underscore instead of hyphen


    2.  Enabling my phone to connect to my laptop's IP address at http://10.240.120.2:4242
        sp that it can access the endpointof this flask app:
        Ref: ShatOpenai
        i. In main, I did this: app.run(host='0.0.0.0', port=4242, debug=True)
            the host='0.0.0.0' ensures that flask is running and listening on all my device's
            IP address.
            However, I could set it to "10.240.120.2"

            Also, I had to make a rule in my firewall settings, an *inbound* rule to allow inbound connections to go through into my computer.
            It is quite dangerous, I think.

        ii. as well as in 'base_script.py', I changed the servr name to http://10.240.120.2:4242
        using: app.config["SERVER_NAME"] = "10.240.120.2:4242"

        But it still didn't work out. So I just switched back to using localhost:4242
        and the email will contain this same link.
        I know its not suitable for production. I'll learn

    3.  Indeed, accourding to my speculation, it turns out that every url ednpoint runs on one thread...
    the tasks on one endpoint have to dinish and return before another endpoin, when hit, can run.

    I found this to be the case when I made one endpooint wait while I tried to hit the '/confirm'
    endpoint to change the flag to make the previous endpoint continue.

    !## Further speculations
    I thought I could run the tasks on each endpoint in their own thread so that another endpoint can be hit and do its own tasks while the proir waits.
    But the issue is not the running of the tasks, but even the commencing of the tasks when that enspoint is hit.
    Why? Because each endpoint has to return control before another can be hit... lest the page on the client-side will be seen to be continually loading, waiting for that endpoint's process to finish.

    Solutions:
    1.  Use normal execution control and more endpoints to product the desired outcome.
    2.  Learn how flask enables asynchronous endpoints.

    ##  Further Speculations
    ### Concerning method 1:
        #   Process
        Now, my image of its working is that when the confirmation link is clicked, the execution
        on the '/verify-email' endpoint should continue
        and hence automatically redirect to the home page.

        But because this doesn't work, and I'm not using asynchronous endpoints, when the email recipient does verify, e.g. with their phone...
        it is not possible to make it redirect on their other device in the first way I considered.

        However, there is this way:
        I made the confirmation page (success.html) that is rendered run a JavaScript that waits for some time and then redirects the user to the home page. So it works just fine.

        Initially, I wanted the confirmation page to be by itself, and then the previous page the user
        opened to automatically redirect to the Home page.
        The server scripts and javascript only work for a particular web page.
        But there are a few ways to do this:
            i.  Have a JavaScript that continually runs on that previous page (the page the user orignially clicked the link from). This Script can continually fetch for the Boolean
            flag that shows login was successful. This can be done simply with a while loop that
            runs on delay.
            ii. If there was a hook that detects when one clicks a page's tab, like when a page is viewed, this can be used to run the block of code to fetch the Boolean flag for successful login.

        In conclusion, I made three scripts for the three cases.
        Out of the three, the normal redirect from the confirmation/success page from email link
        and using the loop worked.