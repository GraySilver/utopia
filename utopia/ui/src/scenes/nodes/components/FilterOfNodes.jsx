import React from "react";
import {Card, CardTitle, Badge, CustomInput} from "reactstrap";

import getConnectedAndNotConnectedNode from "util/index";

const FilterOfNodes = props => {
    const {nodes, checks, onInputChange} = props;
    const {connectedNodes, notConnectedNodes} = getConnectedAndNotConnectedNode(
        nodes
    );
    let nodesLength = 0;
    let groupLength = 0;
    for(let i = 0; i < connectedNodes.length;i++){
        connectedNodes[i].general.meta === "group" ? (
            groupLength += 1
        ):(
            nodesLength += 1
        )
    }



    return (
        <React.Fragment>
            <Card body>
                <CardTitle>
                    Groups <Badge color="secondary">{groupLength}</Badge>
                </CardTitle>
                {connectedNodes.map(node => (
                    node.general.meta === "group" ? (

                        <CustomInput
                            key={node.general.name}
                            type="checkbox"
                            name={node.general.name}
                            id={node.general.name}
                            label={node.general.name}
                            onChange={onInputChange}
                            checked={checks.indexOf(node.general.name) >= 0}
                            inline
                        />) : ("")
                ))}
                <br></br>
                <CardTitle>
                    Nodes <Badge color="secondary">{nodesLength}</Badge>
                </CardTitle>
                {connectedNodes.map(node => (
                    node.general.meta === "node" ? (

                        <CustomInput
                            key={node.general.name}
                            type="checkbox"
                            name={node.general.name}
                            id={node.general.name}
                            label={node.general.name}
                            onChange={onInputChange}
                            checked={checks.indexOf(node.general.name) >= 0}
                            inline
                        />) : ("")
                ))}
                <br></br>
            {/*<Card body>*/}
            {/*    <CardTitle>*/}
            {/*        Connected <Badge color="secondary">{connectedNodes.length}</Badge>*/}
            {/*    </CardTitle>*/}
            {/*    {connectedNodes.map(node => (*/}
            {/*        <CustomInput*/}
            {/*            key={node.general.name}*/}
            {/*            type="checkbox"*/}
            {/*            name={node.general.name}*/}
            {/*            id={node.general.name}*/}
            {/*            label={node.general.name}*/}
            {/*            onChange={onInputChange}*/}
            {/*            checked={checks.indexOf(node.general.name) >= 0}*/}
            {/*            inline*/}
            {/*        />*/}
            {/*    ))}*/}
            {/*</Card>*/}
            {/*<Card body>*/}
                <CardTitle>
                    Not-Connected{" "}
                    <Badge color="secondary">{notConnectedNodes.length}</Badge>
                </CardTitle>
                {notConnectedNodes.map(node => (
                    <CustomInput
                        key={node.general.name}
                        type="checkbox"
                        name={node.general.name}
                        id={node.general.name}
                        label={node.general.name}
                        onChange={onInputChange}
                        disabled
                    />
                ))}
            </Card>
        </React.Fragment>
    );
};

export default FilterOfNodes;
