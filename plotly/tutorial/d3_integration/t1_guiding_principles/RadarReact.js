class RadarPie extends Component {
  constructor(props) {
    super(props);
    this.getRef = this.getRef.bind(this);
  }

  componentDidMount() {
    RadarPieD3.create(this.el, this.props.fig);
  }

  componentWillUnmount() {
    RadarPieD3.destroy(this.el);
  }

  componentDidUpdate() {
    RadarPieD3.update(this.el, this.props.fig);
  }

  render() {
    return <div ref={el => this.el = el} />;
  }
}
