package ObjectOriented;

class SpaceShipControls {
	void up(int velocity) {}
	void down(int velocity) {}
	void left(int velocity) {}
	void right(int velocity) {}
	void forward(int velocity) {}
	void back(int velocity) {}
	void turboBoost() {}
}
public class SpaceShipDelegation {

	/**
	 * @param args
	 */
	private String name;
	private SpaceShipControls controls = new SpaceShipControls();
	public SpaceShipDelegation(String name){
		this.name = name;
	}
	// Delegated methods
	public void back(int velocity){
		controls.back(velocity);
	}
	public void up(int velocity){
		controls.up(velocity);
	}
	public void down(int velocity){
		controls.down(velocity);
	}
	public void forward(int velocity){
		controls.forward(velocity);
	}
	public void left(int velocity){
		controls.left(velocity);
	}
	public void right(int velocity){
		controls.right(velocity);
	}
	public void turboBoost(){
		controls.turboBoost();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SpaceShipDelegation protector = new SpaceShipDelegation("NSEA Protector");
		protector.forward(100);
	}

}
