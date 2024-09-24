from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'oMonDemo',    # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0f0000, 'k8conf', [c for c in 'set +C ; export KUBECONFIG=${HOME}/admin.conf']),
        (0x0f0000, 'kind',   [c for c in 'cd ~/dev/ovn-kubernetes.git/contrib && ./kind.sh && IMG="quay.io/fedora/fedora:latest" ; docker pull $IMG ; CLUSTER=ovn ; kind load docker-image $IMG --name $CLUSTER && echo ok']),
        (0x0f0000, 'clone', [c for c in 'cd ~/dev && git clone https://github.com/amorenoz/ovsdb-mon.git && cd ~/dev/ovsdb-mon']),
        # 2nd row ----------
        (0x000000, 'srcOVN',    [c for c in 'cd ~/dev/ovsdb-mon/dist && source ./ovsdb-mon-ovn.source']),
        (0x000000, 'NBmon', [c for c in 'ovsdb-mon.nb']),
        (0x000000, 'srcOVS',    [c for c in 'cd ~/dev/ovsdb-mon/dist && source ./ovsdb-mon-ovs.source']),
        # 3rd row ----------
        (0x000000, 'nbLSP', [c for c in 'list logical_switch_port --filter name=default_fedora uuid name addresses up options']),
        (0x000000, 'k8RUN', [c for c in 'kubectl run -i --tty --rm fedora --image=quay.io/fedora/fedora:latest --restart=Never -- bash -il']),
        (0x000000, 'SBmon', [c for c in 'ovsdb-mon.sb -auto -monitor Logical_Flow,Port_Binding']),
        # 4th row ----------
        (0x000000, 'wrkOF', [c for c in 'ovsdb-mon.ovs.ovn-worker list Interface Name Ofport ExternalIDs']),
        (0x000000, 'wk2OF', [c for c in 'ovsdb-mon.ovs.ovn-worker2 list Interface Name Ofport ExternalIDs']),
        (0x000000, 'gpod', [c for c in 'kubectl get pod -o wide']),
        # Encoder button ---
        (0x000000, '', [c for c in 'https://github.com/amorenoz/ovsdb-mon.git'])
    ]
}

