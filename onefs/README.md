These templates (importing the xml will import 2 templates) are for monitoring
Isilon storage devices, known as OneFS.  The items are gathered via SNMPv2
polls.  The "Cluster" template is meant to monitor the SmartConnect IP (the
IP that floats between all the nodes).  The "Node" template is meant to
monitor individual nodes.  You can apply both templates to either the
SmartConnect IP or to an individual node IP but you will likely see duplicate
items or triggers tripping false positives.
