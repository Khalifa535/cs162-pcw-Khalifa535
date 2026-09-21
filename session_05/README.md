# CS162 Session 5: Making HTTP requests

This is local pre-class preparation for Session 5. Review and edit it before
committing or pushing it to GitHub.

## 1. httpbin form

**Complete:** Khalifa filled and submitted `https://httpbin.org/forms/post` in
Chrome DevTools. The Network panel showed a successful POST to `/post` with
status 200; he inspected the payload and the JSON response that echoed the
submitted fields. Screenshot evidence was shared in chat, not saved in this
folder. The key things to explain are:

- the form uses `method="post"` and sends data to `/post`;
- each control has a `name`, which becomes the key sent to the server;
- the Network tab shows a POST request after submit;
- the response echoes the submitted form fields.

## 2. Kanban form

The file `index.html` contains a minimal form for a short task description,
ready to paste into the class document. Khalifa viewed its browser preview.
Submitting to `/tasks` returns `501` in the static preview server because no
server route is implemented; this exercise only requires the form markup.

Important form ideas:

- `action="/tasks"` says where the browser would send the form.
- `method="post"` says the task text should be sent in the request body.
- `name="task"` is the key a server would read from the submitted form.
- `required` stops empty submissions before the request is made.

## 3. httpbin Python

The file `httpbin_requests.py` uses the `requests` library to:

- log in with basic auth;
- download an image;
- generate a UUID4 from httpbin;
- return a simple JSON response.

Run it with:

```bash
python3 -m pip install requests
python3 session_05/httpbin_requests.py
```

The script was run successfully: all four requests returned status 200. It
prints each request method and URL, response status and headers, and the text
response data. The PNG response is saved as bytes instead of printed; the
downloaded file was verified as a valid 100-by-100 PNG.

## Optional public API

Not done yet. A good optional extension would be to query a small public API and
print the response status code plus one or two parsed JSON fields.

## Before class

- Review the form and Python script so Khalifa can explain each line in his own
  words.
- Add any question for class to the Forum workbook if useful. Its editor was
  blank when last inspected; no response has been entered or submitted.
- The course README requires PCW work to be committed and pushed before class.
