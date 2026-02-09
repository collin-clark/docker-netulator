from flask import Flask, jsonify, render_template, request
import ipaddress
from netaddr import IPNetwork

app = Flask(__name__)

@app.route('/')
def ipcalc():
    return render_template('ipcalc.html')

@app.route('/ipcalc_results')
def ipcalc_results():
    raw = (request.args.get('ipaddy') or "").strip()
    if not raw:
        return jsonify({
            "status": "error",
            "message": "Enter a network as IP/CIDR (e.g., 192.168.1.10/24) or IP MASK (e.g., 192.168.1.10 255.255.255.0)."
        }), 400

    # Normalize "IP MASK" -> "IP/MASK", keep "IP/CIDR" as-is
    normalized = "/".join(raw.split())  # splits on any whitespace, not just one space

    try:
        ipaddr = ipaddress.IPv4Network(normalized, strict=False)  # allows host bits
    except ValueError as e:
        log.warning("Invalid ipcalc input: raw=%r normalized=%r error=%s", raw, normalized, e)
        return jsonify({
            "status": "error",
            "message": "Invalid network. Use IP/CIDR (192.168.1.10/24) or IP MASK (192.168.1.10 255.255.255.0).",
            "detail": str(e)  # remove this line if you don't want to show specifics
        }), 400

    # If you want to keep netaddr for the rest, convert to string
    ipnet = IPNetwork(str(ipaddr))
    ipnetnetwork = ipnet.network
    ipnetbroadcast = ipnet.broadcast
    ipnetnetmask = ipnet.netmask
    ipnetcidr = ipnet.cidr
    ipnetprefix = ipnet.prefixlen
    ipnethostmask = ipnet.hostmask
    ipnetsize = ipnet.size
    iphostsize = (ipnetsize - 2)
    ipnetfirst = ipnet[1] if ipnetsize > 2 else None
    ipnetlast = ipnet[-2] if ipnetsize > 2 else None
    ipnetnetworkbits = ipnet.network.bits()
    ipnetnetmaskbits = ipnet.netmask.bits()
    ipnet_1 = ipnet.next(-1)
    ipnet_2 = ipnet.next(-2)
    ipnet_3 = ipnet.next(-3)
    ipnet1 = ipnet.next(1)
    ipnet2 = ipnet.next(2)
    ipnet3 = ipnet.next(3)
    supernets = ipnet.supernet(8)
#   Create subnets inside the CIDR entered
    subnets30 = list(ipnet.subnet(30))
    subnets29 = list(ipnet.subnet(29))
    subnets28 = list(ipnet.subnet(28))
    subnets27 = list(ipnet.subnet(27))
    subnets26 = list(ipnet.subnet(26))
    subnets25 = list(ipnet.subnet(25))
    subnets24 = list(ipnet.subnet(24))
    subnets23 = list(ipnet.subnet(23))
    subnets22 = list(ipnet.subnet(22))
    subnets21 = list(ipnet.subnet(21))
    subnets20 = list(ipnet.subnet(20))
    subnets19 = list(ipnet.subnet(19))
    subnets18 = list(ipnet.subnet(18))
    subnets17 = list(ipnet.subnet(17))
    subnets16 = list(ipnet.subnet(16))
    subnets15 = list(ipnet.subnet(15))
    subnets14 = list(ipnet.subnet(14))
    subnets13 = list(ipnet.subnet(13))
    subnets12 = list(ipnet.subnet(12))
    subnets11 = list(ipnet.subnet(11))
    subnets10 = list(ipnet.subnet(10))
    subnets9 = list(ipnet.subnet(9))
    subnet_1 = ipnetprefix + 1
    subnet_2 = ipnetprefix + 2
    subnet_3 = ipnetprefix + 3
    subnet_4 = ipnetprefix + 4
    subnet_5 = ipnetprefix + 5

    if subnet_5 > 32:
        subnet_5 = 32
        subnet_gen5 = list(ipnet.subnet(subnet_5))
    else:
        subnet_gen5 = list(ipnet.subnet(subnet_5))

    if subnet_4 > 32:
        subnet_4 = 32
        subnet_gen4 = list(ipnet.subnet(subnet_4))
    else:
        subnet_gen4 = list(ipnet.subnet(subnet_4))

    if subnet_3 > 32:
        subnet_3 = 32
        subnet_gen3 = list(ipnet.subnet(subnet_3))
    else:
        subnet_gen3 = list(ipnet.subnet(subnet_3))

    if subnet_2 > 32:
        subnet_2 = 32
        subnet_gen2 = list(ipnet.subnet(subnet_2))
    else:
        subnet_gen2 = list(ipnet.subnet(subnet_2))

    if subnet_1 > 32:
        subnet_1 = 32
        subnet_gen1 = list(ipnet.subnet(subnet_1))
    else:
        subnet_gen1 = list(ipnet.subnet(subnet_1))

    # Render the template and pass it the variables from this script
    return render_template('ipcalc_results.html',
        ipaddr=ipaddr,
        ipnet=ipnet,
        ipnetnetwork=ipnetnetwork,
        ipnetbroadcast=ipnetbroadcast,
        ipnetnetmask=ipnetnetmask,
        ipnetcidr=ipnetcidr,
        ipnetprefix=ipnetprefix,
        ipnethostmask=ipnethostmask,
        ipnetsize=ipnetsize,
        iphostsize=iphostsize,
        ipnetfirst=ipnetfirst,
        ipnetlast=ipnetlast,
        ipnetnetworkbits=ipnetnetworkbits,
        ipnetnetmaskbits=ipnetnetmaskbits,
        ipnet_1=ipnet_1,
        ipnet_2=ipnet_2,
        ipnet_3=ipnet_3,
        ipnet1=ipnet1,
        ipnet2=ipnet2,
        ipnet3=ipnet3,
        supernets=supernets,
        subnets30=subnets30,
        subnets29=subnets29,
        subnets28=subnets28,
        subnets27=subnets27,
        subnets26=subnets26,
        subnets25=subnets25,
        subnets24=subnets24,
        subnets23=subnets23,
        subnets22=subnets22,
        subnets21=subnets21,
        subnets20=subnets20,
        subnets19=subnets19,
        subnets18=subnets18,
        subnets17=subnets17,
        subnets16=subnets16,
        subnets15=subnets15,
        subnets14=subnets14,
        subnets13=subnets13,
        subnets12=subnets12,
        subnets11=subnets11,
        subnets10=subnets10,
        subnets9=subnets9,
        subnet_gen1=subnet_gen1,
        subnet_gen2=subnet_gen2,
        subnet_gen3=subnet_gen3,
        subnet_gen4=subnet_gen4,
        subnet_gen5=subnet_gen5,
        subnet_1=subnet_1,
        subnet_2=subnet_2,
        subnet_3=subnet_3,
        subnet_4=subnet_4,
        subnet_5=subnet_5
        )

# The development server
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
