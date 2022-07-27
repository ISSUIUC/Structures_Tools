import pydot
import xmltodict
import pprint

pp = pprint.PrettyPrinter(indent = 0)
inf = open("test_rockets/simple.ork", 'r')
xml_string = inf.read()
inf.close()
xml_dict = xmltodict.parse(xml_string)
pp.pprint(xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"])
def draw(parent_name, child_name):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

def visit(node, parent = None):
    print(node)
    try:
        for k,v in node.iteritems():
            if (type(v) is dict):
                # We start with the root node whose parent is None
                # we don't want to graph the None node
                if parent:
                    draw(parent, k)
                visit(v, k)

            else:
                draw(parent, k)
                # drawing the label using a distinct name
                draw(k, k+'_'+v)
    except:
        print("oof")

graph = pydot.Dot(graph_type='graph')

visit(xml_dict["openrocket"]["rocket"]["subcomponents"]["stage"])

graph.write_png('example1_graph.png')
