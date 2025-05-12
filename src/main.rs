#[macro_use]
extern crate rocket;

mod routes;

use rocket::fs::{relative, FileServer};
use rocket_dyn_templates::Template;

use rocket::shield::{Frame, Shield};

#[launch]
fn rocket() -> _ {
    let shield: Shield = Shield::default().disable::<Frame>();
    rocket::build()
        .mount("/", routes![routes::index])
        .mount("/public", FileServer::from(relative!("static")))
        .attach(Template::fairing())
        .attach(shield)
}
