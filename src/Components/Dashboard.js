import React, { Component } from "react";
import "react-bootstrap-table-next/dist/react-bootstrap-table2.min.css";
import { Container, Jumbotron, Button, Card } from "react-bootstrap";
import { Link } from "react-router-dom";
import BootstrapTable from "react-bootstrap-table-next";
import axios from "axios";

class Dashboard extends Component {
  

  state = {
    shippingdata: [],
  };

  componentDidMount() {
    axios
      .get(`http://shipping-sop.herokuapp.com/shipping/dashboard/1/?fbclid=IwAR0T7TDOCz8nmCVuIZzxYz-BiTIlOCJaxtT3H0wYbQC5Vq2NSldkjuYLZD0&format=json`)
      .then((res) => {
        res.data.map((item) => {
          axios
          .get(`http://shipping-sop.herokuapp.com/shipping/orderItem/description/${item.shippingid}/`)
          .then((res) => {
            const datashipping = {
              'id': item.id,
              'name' : item.carrier.name,
              'reciever' : item.reciever,
              'sender' : item.sender,
              'shippingid' : item.shippingid,
              'status' : res.data[0].status
             }
              const updatearray = [...this.state.shippingdata, datashipping]
              this.setState({
                shippingdata : updatearray
              })


          })
          .catch((er) => console.log(er))
        })
      })
      .catch((er) => console.log(er))
  }

  

  render() {
    const columns = [
      {
        dataField: "id",
        text: "ID",
      },
      {
        dataField: "name",
        text: "Transport",
      },
      {
        dataField: "reciever",
        text: "Reciever",
      },
      {
        dataField: "sender",
        text: "Sender",
      },
      {
        dataField: "shippingid",
        text: "Tracking ID",
      },
      {
        dataField: "status",
        text: "Status",
      },
      {
        dataField: "action",
        text: "Actions",
        formatter: (rowContent, row, formatExtraData) => {
          return (
            <Link to= {{
              pathname: '/Home',
              idShipping :{
                id: row.shippingid
              }
            }}>
              <Button>Check</Button>
            </Link> 
          )
        }
      },
    ];

    const countOrdered = this.state.shippingdata.filter(item => item.status == 'Ordered')
    const countShipped = this.state.shippingdata.filter(item => item.status == 'Shipped')
    const countReady = this.state.shippingdata.filter(item => item.status == 'Ready')
    const countDelivered= this.state.shippingdata.filter(item => item.status == 'Delivered')

    return (
      <div>
        <Container fluid>
          <div className="m-5">
            <p style={{ fontSize: 50 }}>OVERVIEW</p>
            <div className="row d-flex justify-content-between">
              <Card
                className="shadow-lg bg-info"
                style={{ width: "20rem", marginTop: 20 }}
              >
                <Card.Body>
                  <Card.Title className="py-3">
                    <p className="h2 text-uppercase text-white font-weight-bold">
                      ordered
                    </p>
                    <hr />
                  </Card.Title>
                  <Card.Text className="py-3">
                    <p className="display-4 float-right font-weight-bold text-white">
                      {countOrdered.length}
                    </p>
                  </Card.Text>
                </Card.Body>
              </Card>
              <Card
                className="shadow-lg bg-primary"
                style={{ width: "20rem", marginTop: 20 }}
              >
                <Card.Body>
                  <Card.Title className="py-3">
                    <p className="h2 text-uppercase text-white font-weight-bold">
                      shipped
                    </p>
                    <hr />
                  </Card.Title>
                  <Card.Text className="py-3">
                    <p className="display-4 float-right font-weight-bold text-white">
                      {countShipped.length}
                    </p>
                  </Card.Text>
                </Card.Body>
              </Card>
              <Card
                className="shadow-lg bg-danger"
                style={{ width: "20rem", marginTop: 20 }}
              >
                <Card.Body>
                  <Card.Title className="py-3">
                    <p className="h2 text-uppercase text-white font-weight-bold">
                      Ready
                    </p>
                    <hr />
                  </Card.Title>
                  <Card.Text className="py-3">
                    <p className="display-4 float-right font-weight-bold text-white">
                      {countReady.length}
                    </p>
                  </Card.Text>
                </Card.Body>
              </Card>
              <Card
                className="shadow-lg bg-success"
                style={{ width: "20rem", marginTop: 20 }}
              >
                <Card.Body>
                  <Card.Title className="py-3">
                    <p className="h2 text-uppercase text-white font-weight-bold">
                      Finish
                    </p>
                    <hr />
                  </Card.Title>
                  <Card.Text className="py-3">
                    <p className="display-4 float-right font-weight-bold text-white">
                      {countDelivered.length}
                    </p>
                  </Card.Text>
                </Card.Body>
              </Card>
            </div>
          </div>
          <hr />
          <Container fluid>
            <Jumbotron
              className="bg-white shadow-lg"
              style={{ borderRadius: 30, backgroundColor: "gray" }}
            >
              <p style={{ fontSize: 50, justifyContent: "center" }}>
                Secondary
              </p>
              <BootstrapTable
                rowStyle={{
                  fontSize: 20,
                  fontWeight: "lighter",
                }}
                headerClasses="h3 border-5"
                keyField="id"
                data={this.state.shippingdata}
                columns={columns}
              />
            </Jumbotron>
          </Container>
        </Container>
      </div>
    );
  }
}

export default Dashboard;
