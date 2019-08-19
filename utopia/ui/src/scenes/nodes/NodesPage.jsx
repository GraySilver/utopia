import React, { Component } from "react";
import { Row, Col, Container } from "reactstrap";

import Processes from "common/helpers/Processes";
import FilterOfNodes from "scenes/nodes/components/FilterOfNodes";

class NodesPage extends Component {
  state = {
    checks: [],
    check_count: 0
  };

  handleInputChange = event => {
    const target = event.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;
    if (value) {
      this.setState(prevState => ({
        checks: prevState.checks.concat([name])
      }));
    } else {
      this.setState(prevState => ({
        checks: prevState.checks.filter(element => element !== name)
      }));
    }
  };


  componentDidMount() {
    this.props.refreshNodes();
    this.timer = setInterval(() => {
            console.log('refreshNodes Now.');
            this.props.refreshNodes();
        }, 60000);
  }

  componentWillUnmount() {
        // 在unmount回调清除定时器
        this.timer && clearInterval(this.timer);
  }

  render() {
    // Connecting Node小于3的时候自动全启
    if (this.props.nodes.length <= 3){
         this.state.check_count += 1;
      if (this.state.check_count == 2) {
        for (let i = 0 ;i<this.props.nodes.length;i++){
          this.state.checks.push(this.props.nodes[i].general.name)
        }
        this.state.check_count += 1
    }
    }
    const { checks } = this.state;
    const { nodes, refreshNodes } = this.props;

    return (
      <Container fluid>
        <Row >
          <Col sm={{ size: "auto" }}>
            <FilterOfNodes
              nodes={this.props.nodes}
              checks={checks}
              onInputChange={this.handleInputChange}
            />
          </Col>
          <Col>
            {nodes
              .filter(node => checks.indexOf(node.general.name) >= 0)
              .map(node => (
                <Processes
                  key={node.general.name}
                  node={node}
                  refresh={refreshNodes}
                />
              ))}
          </Col>
        </Row>
      </Container>
    );
  }
}

export default NodesPage;
