class Message(val person: String) {
    val greeting = "Hello"

    fun sayHello(): String {
        return "$greeting $person"
    }
}

fun main(args: Array<String>) {
    val m = Message("Mary")
    println(m.sayHello())
}